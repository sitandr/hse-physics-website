from ..models import Announcement, Profile, MarkdownPage

from django import forms


class WriteAnnounceForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["name", "text"]
        # exclude = ["sender", "receivers"]  # user must't be able to edit these


class WriteLectorsForm(WriteAnnounceForm):
    course_number = forms.ChoiceField(label='Курс', choices=[(i, i) for i in range(1, 4 + 1)],
                                      initial=(1))


class CreateMarkdownPageForm(forms.ModelForm):
    class Meta:
        model = MarkdownPage
        fields = ['text']
