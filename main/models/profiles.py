from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

LECT_ROLE = 'Преподаватель'
STUD_ROLE = 'Студент'


from .models import EmailUser, Group

class Profile(models.Model):
    user = models.OneToOneField(EmailUser, on_delete = models.CASCADE)
    
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    
    
    groups = models.ManyToManyField(Group)
                            
    #college = models.CharField(max_length=30, default = 'HSE')
    #major = models.CharField(max_length=30, default = 'Physics')

    def __str__(self):
        return 'anonym'
        #return ' '.join([self.first_name, self.second_name])

#@receiver(post_save, sender=EmailUser)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=EmailUser)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

class Lecturer(Profile):
    role = LECT_ROLE
    def __str__(self):
        return 'a lect'
        #return ' '.join([self.first_name,
        #                self.patronymic,
        #                self.second_name])

class Student(Profile):
    course = models.CharField(max_length=30)
    program_level = models.CharField(max_length=30)
    course_number = models.IntegerField()
    
    role = STUD_ROLE
    def __str__(self):
        return 'a stud'
        #return ' '.join([self.first_name,
        #                self.patronymic,
        #                self.second_name])

class Administrator(Profile):
    role = 'Администратор'
    def __str__(self):
        return ' '.join([self.first_name,
                        self.patronymic,
                        self.second_name, '(администратор)'])

roles = {LECT_ROLE: Lecturer,
         STUD_ROLE: Student,
         '': Profile,}


