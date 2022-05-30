from ..models import Task, CoursePage, File
from django.forms import ModelForm, TextInput, Textarea


class MaterialForm(ModelForm):
    class Meta:
        model = File
        fields = ('name', 'description', 'file_material',)

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
