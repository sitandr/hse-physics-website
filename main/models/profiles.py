from django.db import models
from .models import Group


class Profile(models.Model):
    NO_ROLE = ''
    LECT_ROLE = 'Преподаватель'
    STUD_ROLE = 'Студент'

    roles_repr = {NO_ROLE: 'Аноним ', LECT_ROLE: LECT_ROLE,
                  STUD_ROLE: STUD_ROLE}

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)

    photo = models.ImageField(upload_to='profiles', blank=True)
    groups = models.ManyToManyField(Group, blank=True)

    @property
    def role(self):
        "Important: doesn't concretize user"
        return self.user.role

    # for students

    course = models.CharField(max_length=30, blank=True)
    program_level = models.CharField(max_length=30, blank=True)
    course_number = models.IntegerField(null=True, blank=True)

    # for lectors

    link = models.URLField(max_length=200, blank=True)
    story = models.TextField(blank=True)

    # college = models.CharField(max_length=30, default = 'HSE')
    # major = models.CharField(max_length=30, default = 'Physics')

    def get_full_name(self):
        return ' '.join([self.first_name,
                         self.last_name,
                         self.patronymic, ])

    def __str__(self):
        child = self.user.concretize()
        return ((self.roles_repr[child.role] if child.role in self.roles_repr
                 else 'unknown') + ' ' + self.get_full_name())
