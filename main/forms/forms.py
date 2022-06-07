from embed_video.fields import EmbedVideoFormField

from ..models import File, Url, Video, MarkdownMat, MaterialContainer, IFrame, CoursePage, Block
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

    def clean(self):
        form_data = self.cleaned_data
        if not any(form_data):
            self.add_error("Добавьте текст/материалы")
        return form_data

    def save(self, parent=None):

        # this code is terrible, it would be wonderful to rewrite it
        m_text, u_m, v_m, file_m, frame_m = (self.cleaned_data["markdown_text"], self.cleaned_data["url_material"],
                                             self.cleaned_data["video_material"], self.cleaned_data["file_material"],
                                             self.cleaned_data["frame_url"])

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

        if file_m:
            f = File()
            f.file_material = file_m
            f.name = file_m.name
            f.save()
            c.files.add(f)

        if frame_m:
            frame = IFrame()
            frame.frame_url = frame_m
            frame.save()
            c.frames.add(frame)

        c.parent = parent
        c.save()

        return c


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
        fields = ['general_info', 'main_lecturer']
