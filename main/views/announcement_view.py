from .. import models

from django.shortcuts import render, redirect
from ..models import Announcement
from django.core.exceptions import PermissionDenied


def show_announcements(request, edit=False):
    "display any user profile's, probably trying to edit"

    user = request.user.concretize()
    viewed_ann = []

    if user.role == models.profiles.Profile.LECT_ROLE:
        ...
    elif user.role == models.profiles.Profile.STUD_ROLE:
        viewed_ann = user.recieved_announcements.filter(receivers__profile__course=user.profile.course)
        ...
    else:
        raise PermissionDenied("You are not student/lecturer")

    return render(request, 'main/announcements.html', {'user': user,
                                                       'edit': edit,
                                                       'viewed_ann': viewed_ann})
