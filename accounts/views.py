from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms

from main.models import EmailUser, profiles

class BasicRegistrationForm(UserCreationForm):

    # this string is important because it allows to edit username
    first_name = forms.CharField(label='Имя',
                         widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия',
                         widget=forms.TextInput(attrs={'class': 'form-input'}))

    password1 = forms.CharField(label='Пароль',
                          widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    password2 = forms.CharField(label='Повтор пароля',
                          widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-input'}), required = True)

    
    class Meta:
        model = EmailUser
        fields = ('first_name', 'last_name',
                  'email', 'password1',
                  'password2')

    def save(self, commit=True, role = ''):
        first_name = self.cleaned_data["first_name"]
        second_name = self.cleaned_data["last_name"]
        
        user = EmailUser.objects.create_user(email=self.cleaned_data["email"],
                                             password=self.cleaned_data["password1"],
                                             role = role)
        print('! Email create_user call')

        user.username = first_name + '_' + second_name # using space will cause problems with admin site
       # user = super(ExtendedEmailUserCreationForm, self).save(commit=False)
        user.profile.first_name = first_name
        user.profile.last_name = second_name # DEBUG!!!
        print('saving names:', user.profile.first_name, user.profile.last_name )
        
        if commit:
            user.save()
            user.profile.save()
            
        return user

class StudentForm(BasicRegistrationForm):
    course = forms.ChoiceField(choices =
                            [('Физика', 'Физика'),
                            ('ПМИ', 'ПМИ')],
                            initial = ('Физика', 'Физика'))
    
    program_level = forms.ChoiceField(choices =
                            [('Бакалавриат', 'Бакалавриат'),
                            ('Магистратура', 'Магистратура')],
                            initial = ('Бакалавриат', 'Бакалавриат'))
    
    course_number = forms.ChoiceField(choices =
                            [(i, i) for i in range(1, 4 + 1)],
                            initial = (1))

    class Meta:
        model = EmailUser
        fields = BasicRegistrationForm.Meta.fields + ('course', 'program_level', 'course_number')

    def save(self, commit=True):
        # print(super())
        user = super().save(commit=False, role=profiles.STUD_ROLE)
        user.profile.course = self.cleaned_data["course"]
        user.profile.program_level = self.cleaned_data["program_level"]
        user.profile.course_number = self.cleaned_data["course_number"]
        
        if commit:
            user.save()
            user.profile.save()
            print('after saving; here ' + str(type(user.profile)))

        return user

class SignUpView(generic.CreateView):
    form_class = StudentForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
