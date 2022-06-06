from django.db import models
from embed_video.fields import EmbedVideoField

from model_utils.managers import InheritanceManager
from django.template import Template, Context
from ..other.markdown import generate_html


class MaterialMaster(InheritanceManager):
    pass


class Material(models.Model):
    objects = MaterialMaster()
    parent = models.ForeignKey('Block', on_delete=models.CASCADE, null=True, related_name='materials')

    # master = models.ForeignKey(MaterialMaster)

    @property
    def view(self):
        pass

    def concretize(self):
        "return inherited version of self"
        return Material.objects.get_subclass(id=self.id)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ['-id']


class Url(Material):
    address = models.URLField(max_length=200)
    text = models.TextField()

    @property
    def view(self):
        return f'<a href="{self.address}">{self.text}</a>'


class File(Material):
    file_material = models.FileField(null=True, upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)

    @property
    def view(self):
        return f'<a href="{self.file_material.url}" download>{self.name}</a>'


class Video(Material):
    video_material = EmbedVideoField()
    name = models.CharField(max_length=30)

    # class Meta:
    #     verbose_name_plural = "Video"

    def __str__(self):
        return str(self.video_material)

    @property
    def view(self):
        return Template(f'''{{% load embed_video_tags %}}
        {{% video material '600x400' %}}''').render(Context({'material': self.video_material}))
#
# class Google_Sheet(Material):
#     pass


class MarkdownMat(Material):
    text = models.TextField(blank=True)

    @property
    def view(self):
        return generate_html(self.text)


class MaterialContainer(Material):
    markdown = models.ForeignKey(MarkdownMat, on_delete=models.CASCADE)
    urls = models.ManyToManyField(Url)
    videos = models.ManyToManyField(Video)
    files = models.ManyToManyField(File)

    @property
    def view(self):
        return ('═══════<div>' + ''.join(['<div>' + str(m.concretize().view) + '</div>'
                                          for m in [self.markdown] + list(self.urls.all())
                                          + list(self.videos.all()) + list(self.files.all())])
                + '</div>……………')


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    course = models.ForeignKey('CoursePage', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ((str(self.course) + ': ') if self.course else '') + self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Group(models.Model):
    name = models.CharField(max_length=30)
    subgroups = models.ManyToManyField('self')
    parent_grop = models.ForeignKey('self', on_delete=models.CASCADE)
    courses = models.ManyToManyField('CoursePage')
