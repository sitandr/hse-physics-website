from ..models import Task, CoursePage
from django.forms import ModelForm, TextInput, Textarea


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
