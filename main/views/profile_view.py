from .. import models
from django.core.exceptions import PermissionDenied
from ..forms import EditUserForm, EditLecturerForm, EditStudentForm
from ..models import EmailUser
from django.shortcuts import render, redirect, get_object_or_404
from .announcement_view import header_handler


def show_profile(request, user_id, edit=False):
    "display any user profile's, probably trying to edit"

    header_handler(request)

    shown_user = get_object_or_404(EmailUser, id=user_id)
    profile = shown_user.profile

    src_user = shown_user
    shown_user = shown_user.concretize()

    form_class = {models.profiles.Profile.NO_ROLE: EditUserForm,
                  models.profiles.Profile.LECT_ROLE: EditLecturerForm,
                  models.profiles.Profile.STUD_ROLE: EditStudentForm
                  }[shown_user.profile.role]

    error = None
    form = None

    form = form_class(instance=profile)

    if edit:
        if src_user != request.user:
            raise PermissionDenied("Cannot edit this profile")

        if request.method == "POST":
            form = form_class(request.POST, request.FILES, instance=profile)

            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('profile', user_id)
            else:
                error = 'Invalid form'

    return render(request, 'main/profile.html', {'shown_user': shown_user,
                                                 'edit': edit,
                                                 'form': form,
                                                 'error': error})
