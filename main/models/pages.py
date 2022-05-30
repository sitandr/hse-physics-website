from django.db import models
from unidecode import unidecode
from django.urls import reverse
from ..other.markdown import generate_html


class Block(models.Model):
    # contains number of diff. materials, can be anchored to some page
    pass


class CoursePage(models.Model):
    name = models.CharField('Название курса', max_length=50)
    slug = models.SlugField(max_length=255, verbose_name="URL")
    student_block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='page_as_st')
    lecturer_block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='page_as_lect')

    general_info = models.TextField('Общая информация')

    def create_slug(self):  # self-written function for better generating slugs
        self.slug = unidecode(self.name).replace(' ', '_')
        copies = CoursePage.objects.all().filter(slug__startswith=self.slug)
        if copies:
            self.slug += str(len(copies) + 1)

    def __str__(self):
        return self.name

    @property
    def absolute_url(self):
        return reverse('pages', kwargs={'slug': self.slug})


class MarkdownPage(models.Model):

    text = models.TextField()

    @property
    def html(self):
        return generate_html(self.text)
