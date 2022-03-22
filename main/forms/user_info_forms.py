from ..models import Profile
from django import forms
 
class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "photo"]