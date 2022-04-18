from ..models import Announcement

from django import forms


class WriteAnnounceForm(forms.ModelForm):
    class Meta:
        model = Announcement
        # fields = ["text"]
        exclude = ["sender", "receivers"]  # user must't be able to edit these
