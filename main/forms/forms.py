from embed_video.fields import EmbedVideoFormField

from ..models import CoursePage, Block, File, Url, Video, MarkdownMat, Material
from django.forms import ModelForm, TextInput, Textarea, FileField
from django import forms


class MarkdownMatForm(ModelForm):
    class Meta:
        model = MarkdownMat
        fields = ('text',)


class ContainerForm(forms.Form):
    markdown_text = forms.CharField(required=False, widget=Textarea)
    url_material = forms.URLField(required=False)
    video_material = EmbedVideoFormField(required=False)
    file_material = FileField(required=False)
    frame_url = forms.URLField(required=False)


class CreateCourseForm(ModelForm):
    class Meta:
        model = CoursePage
        fields = ["name", "general_info"]
        widgets = {"name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название курса'
        }),
            'general_info': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Общая информация'
            }),
        }

    def save(self, commit=True):
        page = super(ModelForm, self).save(commit=False)
        page.lecturer_block = Block()
        page.lecturer_block.save()
        page.student_block = Block()
        page.student_block.save()
        if commit:
            page.save()
        return page


class EditCourseGeneralInfo(ModelForm):
    class Meta:
        model = CoursePage
        fields = ['general_info']
