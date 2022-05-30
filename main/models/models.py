from django.db import models
from embed_video.fields import EmbedVideoField

from model_utils.managers import InheritanceManager
from django.template import Template, Context
from .pages import Block, CoursePage


class MaterialMaster(InheritanceManager):
    pass


class Material(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    objects = MaterialMaster()
    parent = models.ForeignKey(Block, on_delete=models.CASCADE, null=True, related_name='materials')

    # master = models.ForeignKey(MaterialMaster)

    @property
    def view(self):
        pass

    def concretize(self):
        "return inherited version of self"
        return Material.objects.get_subclass(id=self.id)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Url(Material):
    address = models.URLField(max_length=200)

    @property
    def view(self):
        return Template(f"""<h2>{self.name}:</h2>
    <a href="{self.address}">{self.description}</a>""").render(Context({}))


class File(Material):
    file_material = models.FileField(blank=True, null=True, upload_to='documents')
    is_published = models.BooleanField(default=True)

    @property
    def view(self):
        return Template(f"""<h2>{self.name}</h2>
    <h2>DOWNLOAD FROM HERE<a href="{self.file_material.url}" download>{self.name}</a></h2>""").render(Context({}))


class Video(Material):
    video_material = EmbedVideoField()

    # class Meta:
    #     verbose_name_plural = "Video"

    def __str__(self):
        return str(self.name) if self.name else " "

    @property
    def view(self):
        return Template(f'''{{% load embed_video_tags %}}
        {{% video material '600x400' %}}''').render(Context({'material': self.video_material}))
#
# class Google_Sheet(Material):
#     pass


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    course = models.ForeignKey(CoursePage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ((str(self.course) + ': ') if self.course else '') + self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Group(models.Model):
    name = models.CharField(max_length=30)
    subgroups = models.ManyToManyField('self')
    parent_grop = models.ForeignKey('self', on_delete=models.CASCADE)
    courses = models.ManyToManyField(CoursePage)
