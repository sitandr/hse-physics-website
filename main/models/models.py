from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from unidecode import unidecode
from django.urls import reverse
# from django.conf import settings

from main.models import EmailUser

# EmailUser._meta.get_field('email')._unique = True # make possible log in with email
# EmailUser._meta.get_field('email')._required = True

# from django.contrib.auth.models import EmailUser


class CoursePage(models.Model):
    name = models.CharField('Название курса', max_length=50)
    slug = models.SlugField(max_length=255, verbose_name="URL")
    
    general_info = models.TextField('Общая информация')

    def create_slug(self): # self-written function for better generating slugs
        self.slug = unidecode(self.name).replace(' ', '_')
        copies = CoursePage.objects.all().filter(slug__startswith = self.slug)
        print(copies, len(copies))
        if copies:
            self.slug += str(len(copies) + 1)
    
    def __str__(self):
        return self.name

    @property
    def absolute_url(self):
        return reverse('pages', kwargs={'slug': self.slug})

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    course = models.ForeignKey(CoursePage, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return ((str(self.course) + ': ') if self.course else '') + self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Group(models.Model):
    name = models.CharField(max_length=30)
    subgroups = models.ManyToManyField('self')
    parent_grop = models.ForeignKey('self', on_delete = models.CASCADE)
    courses = models.ManyToManyField(CoursePage)

class Profile(models.Model):
    user = models.OneToOneField(EmailUser, on_delete = models.CASCADE)
    role = models.CharField(max_length=30, choices =
                            [('lecturer', 'Преподаватель'),
                            ('student', 'Студент'),
                            ('administrator', 'Администратор')],
                            default = 'student')
    
    groups = models.ManyToManyField(Group)
                            
    #college = models.CharField(max_length=30, default = 'HSE')
    #major = models.CharField(max_length=30, default = 'Physics')

    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender=EmailUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=EmailUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
