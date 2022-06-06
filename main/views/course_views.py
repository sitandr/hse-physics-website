from django.shortcuts import render, redirect, get_object_or_404
from ..models import Task, CoursePage, Material
from ..forms import TaskForm, CreateCourseForm, EditCourseGeneralInfo
from ..forms import ContainerForm
from django.contrib.auth.decorators import login_required
from ..models import MaterialContainer, MarkdownMat, File, Video, Url, Profile


@login_required
def index(request):
    print(request.user)
    tasks = Task.objects.all()
    materials = MaterialContainer.objects.all()
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


def add_material(request):
    "quite 'clear' method that is capable of suistaining form and creating proper containers"
    if request.method == 'POST':
        form = ContainerForm(request.POST, request.FILES)
        if form.is_valid():
            m_text, u_m, v_m, f_m = (form.cleaned_data["markdown_text"], form.cleaned_data["url_material"],
                                     form.cleaned_data["video_material"], form.cleaned_data["file_material"])
            if any([m_text, u_m, v_m, f_m]):

                t = MarkdownMat()
                t.text = m_text
                t.save()

                c = MaterialContainer(markdown=t)
                c.save()
                if u_m:
                    u = Url()
                    u.address = u_m
                    u.text = u_m
                    u.save()

                    c.urls.add(u)
                if v_m:
                    v = Video()
                    v.video_material = v_m
                    v.save()
                    c.videos.add(v)
                if f_m:
                    f = File()
                    f.file_material = f_m
                    f.name = f_m.name
                    f.save()
                    c.files.add(f)

                c.save()

                return {'posted': True, 'file': c}
    else:
        form = ContainerForm()

    return {'posted': False, 'form': form}


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

    form_1 = TaskForm()
    context = {
        'form_1': form_1,
        'error': error
    }
    return render(request, 'main/create_task.html', context)


def course_page(request, slug, edit_general_info=False):
    page = get_object_or_404(CoursePage, slug=slug)
    if edit_general_info:
        edit_general_info = EditCourseGeneralInfo(instance=page)

        if request.method == "POST":
            form = EditCourseGeneralInfo(request.POST, request.FILES, instance=page)

            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('pages', slug)

    response = add_material(request)

    if response['posted']:
        container = response['file']
        if request.user.concretize().role == Profile.STUD_ROLE:
            container.parent = page.student_block
        else:
            container.parent = page.lecturer_block

        container.save()

        return redirect(request.build_absolute_uri())

    edit_material_form = response['form']

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
