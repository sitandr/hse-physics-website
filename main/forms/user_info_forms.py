from ..models import Profile, Student, Lecturer
from django import forms
 
class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "first_name", "last_name", "patronymic"]

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = EditUserForm.Meta.fields + ["course", "program_level", "course_number"]

class EditLecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = EditUserForm.Meta.fields + ["link", "story"]
