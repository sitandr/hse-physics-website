from django.db import models
from unidecode import unidecode
from django.urls import reverse
from ..other.markdown import generate_html
from django.template import Template, Context
from .profiles import Profile


class Block(models.Model):
    # contains number of diff. materials, can be anchored to some page
    # Page:
    # <Block>   <Block>
    # — Mat      — Mat
    # — Mat      — Mat
    # …
    OF_STUDENT = "student's"
    OF_LECTURER = "lecturer's"
    UNKNOWN = 'unknown'

    @property
    def html(self):
        print('htmling…')
        return ''.join(['<div>' + str(m.concretize().view) + '</div>' for m in self.materials.all()])

    def type_(self):
        if self.pages_as_st.count():
            return Block.OF_STUDENT
        elif self.pages_as_lect.count():
            return Block.OF_LECTURER
        return Block.UNKNOWN

    def can_edit(self, user):
        user = user.concretize()
        return ((user.role == Profile.STUD_ROLE and self.type_ == Block.OF_STUDENT)
                or (user.role == Profile.LECT_ROLE and self.type_ == Block.OF_LECTURER))

    def __str__(self):
        return self.type_() + ' ' + ''.join(map(str, list(self.pages_as_st.all()) + list(self.pages_as_lect.all())))

    @property
    def related_page(self):
        if self.pages_as_st.count():
            return self.pages_as_st.get()
        else:
            return self.pages_as_lect.get()


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


class MarkdownPage(models.Model):

    text = models.TextField()
    name = models.CharField('Название страницы', max_length=50)

    @property
    def html(self):
        return generate_html(self.text)

    def __str__(self):
        return self.name

    @property
    def absolute_url(self):
        return reverse('view_markdown_page', kwargs={"id": self.id})
