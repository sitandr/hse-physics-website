from .. import models

from django.shortcuts import render, redirect
from ..models import Announcement, EmailUser
from django.core.exceptions import PermissionDenied
from ..forms import WriteAnnounceForm


def show_announcements(request, edit=False):
    "display any user profile's, probably trying to edit"

    user = request.user.concretize()
    viewed_ann = []
    form = None

    if user.role == models.profiles.Profile.LECT_ROLE:
        ...
    elif user.role == models.profiles.Profile.STUD_ROLE:
        print(EmailUser.objects.filter(profile__course=user.profile.course))
        viewed_ann = user.recieved_announcements.filter(receivers=user)

        if edit:
            form = WriteAnnounceForm()

            if request.method == "POST":
                form = WriteAnnounceForm(request.POST)

                if form.is_valid():
                    inst = form.save(commit=False)
                    # if course_id:
                    #     inst.course = CoursePage.objects.get(id=course_id).first()
                    inst.sender = user
                    inst.save()

                    inst.receivers.set(EmailUser.objects.filter(profile__course=user.profile.course))

                    return redirect('announce')

    else:
        raise PermissionDenied("You are not student/lecturer")

    return render(request, 'main/announcements.html', {'user': user,
                                                       'edit': edit,
                                                       'viewed_ann': viewed_ann,
                                                       'form': form})
