from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, CoursePage
from .forms import TaskForm, CreateCourseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

def show_profile(request, user_id):
    shown_user = get_object_or_404(User, id=user_id)
    return render(request, 'main/profile.html', {'shown_user': shown_user})
