from django.db import models
from unidecode import unidecode
from django.urls import reverse
from ..other.markdown import generate_html
from django.template import Template, Context


class Block(models.Model):
    OF_STUDENT = "student's"
    OF_LECTURER = "lecturer's"
    UNKNOWN = 'unknown'

    # contains number of diff. materials, can be anchored to some page
    @property
    def html(self):
        print('htmling…')
        return ''.join({'<div>' + str(m.concretize().view) + '</div>' for m in self.materials.all()})

    def type_(self):
        if self.pages_as_st.count():
            return Block.OF_STUDENT
        elif self.pages_as_lect.count():
            return Block.OF_LECTURER
        return Block.UNKNOWN

    def __str__(self):
        return self.type_() + ' ' + ''.join(map(str, list(self.pages_as_st.all()) + list(self.pages_as_lect.all())))


def new_block():
    return Block()


class CoursePage(models.Model):

    name = models.CharField('Название курса', max_length=50)
    slug = models.SlugField(max_length=255, verbose_name="URL")
    student_block = models.ForeignKey(Block, on_delete=models.CASCADE,
                                      related_name='pages_as_st')
    lecturer_block = models.ForeignKey(Block, on_delete=models.CASCADE,
                                       related_name='pages_as_lect')

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

    @property
    def block_html(self):
        return Template('<div class="st_block">' + self.student_block.html + '</div>'
                        + '<div class="lt_block">' + self.lecturer_block.html + '</div>').render(Context({}))


class MarkdownPage(models.Model):

    text = models.TextField()

    @property
    def html(self):
        return generate_html(self.text)
