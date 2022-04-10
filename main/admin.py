from django.contrib import admin
from .models import Task, Profile, CoursePage, Material, Url, File
from .models import EmailUser, StudentUser, LecturerUser
from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display = ('__str__', 'email')

admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(CoursePage)
admin.site.register(EmailUser, UserAdmin)
admin.site.register(StudentUser)
admin.site.register(LecturerUser)
admin.site.register(Material)
admin.site.register(Url)
admin.site.register(File)

