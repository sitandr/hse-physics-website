from django.shortcuts import render, redirect, get_object_or_404
from ..models import Task, CoursePage, Material
from ..forms import TaskForm, CreateCourseForm, MaterialForm, EditCourseGeneralInfo
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    print(request.user)
    tasks = Task.objects.all()
    materials = Material.objects.all()
    courses = CoursePage.objects.all()
    concr_materials = []
    for material in materials:
        concr_materials.append(material.concretize())
    print(concr_materials)
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта',
                   'tasks': tasks,
                   'courses': courses,
                   'materials': concr_materials})


def about(request):
    return render(request, 'main/about.html')


@login_required
def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MaterialForm()
    return render(request, 'main/add_material.html', {
        'form': form
    })


@login_required
def create_task(request, course_id=None):

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


def course_page(request, slug, edit_general_info=False):
    page = get_object_or_404(CoursePage, slug=slug)
    print(edit_general_info)
    if edit_general_info:
        edit_general_info = EditCourseGeneralInfo(instance=page)

        if request.method == "POST":
            form = EditCourseGeneralInfo(request.POST, request.FILES, instance=page)

            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('pages', slug)

    return render(request, 'main/course_page.html', {'page': page,
                                                     'edit_general_info': edit_general_info})


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
