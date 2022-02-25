from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.forms import (CharField, TextInput,
                          PasswordInput, PasswordInput, EmailInput, EmailField)

from main.models import EmailUser

class ExtendedUserCreationForm(UserCreationForm):

    # this string is important because it allows to edit username
    first_name = CharField(label='Имя',
                         widget=TextInput(attrs={'class': 'form-input'}))
    last_name = CharField(label='Фамилия',
                         widget=TextInput(attrs={'class': 'form-input'}))

    password1 = CharField(label='Пароль',
                          widget=PasswordInput(attrs={'class': 'form-input'}))

    password2 = CharField(label='Повтор пароля',
                          widget=PasswordInput(attrs={'class': 'form-input'}))

    email = EmailField(label='Email',
                             widget=EmailInput(attrs={'class': 'form-input'}), required = True)

    
    class Meta:
        model = EmailUser
        fields = ('first_name', 'last_name',
                  'email', 'password1',
                  'password2')

    def save(self, commit=True):
        first_name = self.cleaned_data["first_name"]
        second_name = self.cleaned_data["last_name"]
        

        user = EmailUser.objects.create_user(email=self.cleaned_data["email"], password=self.cleaned_data["password1"])

        user.username = first_name + '_' + second_name # using space will cause problems with admin site
       # user = super(ExtendedEmailUserCreationForm, self).save(commit=False)
        user.first_name = first_name
        user.last_name = second_name
        
        if commit:
            user.save()
            
        return user

class SignUpView(generic.CreateView):
    form_class = ExtendedUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
