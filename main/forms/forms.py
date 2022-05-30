from ..models import Task, CoursePage, Block, File, Url, Video, MarkdownMat, Material
from django.forms import ModelForm, TextInput, Textarea, FileField


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ('name', 'description')


class FileForm(ModelForm):
    file_material = FileField(required=False)

    class Meta:
        model = File
        fields = ('file_material',)


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ('address',)




class VideoForm(ModelForm):
    # video_material = EmbedVideoField(required=False)
    class Meta:
        model = Video
        fields = ('video_material',)


class MarkdownMatForm(ModelForm):
    class Meta:
        model = MarkdownMat
        fields = ('text',)




class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }


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
