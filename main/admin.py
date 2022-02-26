from django.contrib import admin
from .models import Task, Profile, Student, Lecturer, CoursePage
from .models import EmailUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(CoursePage)
admin.site.register(EmailUser, UserAdmin)
