from ..forms import CreateMarkdownPageForm
from ..models import MarkdownPage
from django.shortcuts import render, redirect, get_object_or_404


def create_page(request):

    if request.method == 'POST':
        form = CreateMarkdownPageForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect('view_markdown_page', id=instance.id)

    form = CreateMarkdownPageForm()

    context = {
        'form': form,
        'edit': False
    }
    return render(request, 'main/create_markdown_page.html', context)


def view_page(request, id):
    return render(request, 'main/view_markdown_page.html',
                  {'page': get_object_or_404(MarkdownPage, id=id), 'enable_mathjax': True})


def edit_page(request, id):
    page = get_object_or_404(MarkdownPage, id=id)
    if request.method == 'POST':
        form = CreateMarkdownPageForm(request.POST, request.FILES, instance=page)

        if form.is_valid():
            instance = form.save()
            return redirect('view_markdown_page', id=instance.id)

    form = CreateMarkdownPageForm(instance=page)

    context = {
        'form': form,
        'edit': True
    }
    return render(request, 'main/create_markdown_page.html', context)  # in fact it is "edit", but it is the same
