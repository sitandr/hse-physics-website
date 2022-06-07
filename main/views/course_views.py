from django.shortcuts import render, redirect, get_object_or_404
from ..models import CoursePage, Material
from ..forms import CreateCourseForm, EditCourseGeneralInfo
from ..forms import ContainerForm
from django.contrib.auth.decorators import login_required

from ..models import MaterialContainer
from ..models import Profile, MarkdownPage


@login_required
def index(request):
    materials = MaterialContainer.objects.all()
    courses = CoursePage.objects.all()
    concr_materials = []
    for material in materials:
        concr_materials.append(material.concretize())

    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта',
                   'courses': courses,
                   'markdown_pages': MarkdownPage.objects.all(),
                   'materials': concr_materials})


def about(request):
    return render(request, 'main/about.html')


def course_page(request, slug, edit_general_info=False):
    page = get_object_or_404(CoursePage, slug=slug)
    if edit_general_info:
        edit_general_info = EditCourseGeneralInfo(instance=page)

        if request.method == "POST" and 'edit_general_info' in request.POST:
            form = EditCourseGeneralInfo(request.POST, request.FILES, instance=page)

            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('pages', slug)

    if request.method == 'POST' and 'edit_material_submit' in request.POST:
        edit_material_form = ContainerForm(request.POST, request.FILES)
        # there I'm using same name for bool of state (editing/not) and form, because bool(form) == True

        if edit_material_form.is_valid():
            role = request.user.concretize().role
            edit_material_form.save(parent=(page.student_block if role == Profile.STUD_ROLE else page.lecturer_block))
            return redirect(request.build_absolute_uri())
    else:
        edit_material_form = ContainerForm()

    return render(request, 'main/course_page.html', {'page': page,
                                                     'edit_general_info': edit_general_info,
                                                     'edit_material_form': edit_material_form,
                                                     'enable_mathjax': True})


def remove_material(request, slug, id):
    Material.objects.get(id=id).delete()
    return redirect('pages', slug)


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
