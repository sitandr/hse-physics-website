from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

LECT_ROLE = 'Преподаватель'
STUD_ROLE = 'Студент'


from .models import EmailUser, Group

class Profile(models.Model):
    user = models.OneToOneField(EmailUser, on_delete = models.CASCADE)
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank = True)
    
    
    groups = models.ManyToManyField(Group, blank = True)
                            
    #college = models.CharField(max_length=30, default = 'HSE')
    #major = models.CharField(max_length=30, default = 'Physics')

    def __str__(self):
        return 'anonym ' + ' '.join([self.first_name, self.last_name])

#@receiver(post_save, sender=EmailUser)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

# @receiver(post_save, sender=EmailUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(post_delete, sender=Profile)
def auto_delete_user(sender, instance, **kwargs):
    instance.user.delete()

class Lecturer(Profile):
    role = LECT_ROLE
    link = models.URLField(max_length=200, blank = True)
    def __str__(self):
        return 'a lect'
        #return ' '.join([self.first_name,
        #                self.patronymic,
        #                self.second_name])

class Student(Profile):
    course = models.CharField(max_length=30, blank = True)
    program_level = models.CharField(max_length=30, blank = True)
    course_number = models.IntegerField(null = True, blank = True)
    
    role = STUD_ROLE
    def __str__(self):
        return 'a stud ' + ' '.join([self.first_name,
                                     self.patronymic,
                                     self.last_name])

class Administrator(Profile):
    role = 'Администратор'
    def __str__(self):
        return ' '.join([self.first_name,
                        self.patronymic,
                        self.last_name, '(администратор)'])

roles = {LECT_ROLE: Lecturer,
         STUD_ROLE: Student,
         '': Profile,}


