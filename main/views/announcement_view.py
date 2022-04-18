from .. import models

from django.shortcuts import render, redirect
from ..models import Announcement, EmailUser
from django.core.exceptions import PermissionDenied
from ..forms import WriteAnnounceForm, WriteLectorsForm


def show_announcements(request, edit=False):
    "display any user profile's, probably trying to edit"

    user = request.user.concretize()
    viewed_ann = []
    form = None

    if user.role == models.profiles.Profile.LECT_ROLE:

        viewed_ann = Announcement.objects.all()  # lectors can see all anouncements

        if edit:
            form = WriteLectorsForm()

            if request.method == "POST":
                form = WriteLectorsForm(request.POST)
                print(request.POST)

                if form.is_valid():
                    inst = form.save(commit=False)

                    inst.sender = user
                    inst.save()

                    print()
                    inst.receivers.set(EmailUser.objects.filter(profile__course_number=request.POST['course_number']))
                    # due to the fact "course" is not model field, it is not auto-completed when creating form from request

                    return redirect('announce')

    # I use duplicating code due to the fact that lector/student behaviour may highly vary
    elif user.role == models.profiles.Profile.STUD_ROLE:

        viewed_ann = user.recieved_announcements.all()

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

                    inst.receivers.set(EmailUser.objects.filter(profile__course_number=user.profile.course_number))

                    return redirect('announce')

    else:
        raise PermissionDenied("You are not student/lecturer")

    return render(request, 'main/announcements.html', {'user': user,
                                                       'edit': edit,
                                                       'viewed_ann': viewed_ann,
                                                       'form': form})
