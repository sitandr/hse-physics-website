from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, CoursePage
from .forms import TaskForm, CreateCourseForm, EditUserForm
from django.contrib.auth.decorators import login_required
from .models import EmailUser
from django.core.exceptions import PermissionDenied

@login_required
def index(request):
    tasks = Task.objects.all()
    courses = CoursePage.objects.all()
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта',
                   'tasks': tasks,
                   'courses': courses})


def about(request):
    return render(request, 'main/about.html')

@login_required
def create_task(request, course_id = None):
    
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            inst = form.save(commit=False)
            if course_id:
                inst.course = CoursePage.objects.filter(id=course_id).first()
            inst.save()
                
            return redirect('home')
        else:
            error = 'Ошибка'
    
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_task.html', context)

def course_page(request, slug):
    post = get_object_or_404(CoursePage, slug=slug)
    return render(request, 'main/course_page.html', {'post': post})

@login_required
def create_course(request):
    
    error = ''
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.create_slug()
            instance.save()
            
            return redirect('home')
        else:
            error = 'Ошибка'
    
    form = CreateCourseForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_course.html', context)

def show_profile(request, user_id, mode='edit'):
    "mode can be 'show' or 'edit'"
    shown_user = get_object_or_404(EmailUser, id=user_id)
    profile = shown_user.profile
    error = None

    if mode == "edit":
        if shown_user != request.user:
            return PermissionDenied()

        if request.method == "POST":
            form = EditUserForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
            else:
                error = 'Invalid form'
        else:
            form = EditUserForm(instance=profile)

    return render(request, 'main/profile.html', {'shown_user': shown_user,
                                                 'mode': mode,
                                                 'form': form, 
                                                 'error': error})