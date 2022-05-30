from django.db import models
from . import EmailUser
from django.template import Template, Context

import re
import markdown
from markdown_grid_tables import GridTableExtension

markdown_extensions = ['tables', 'sane_lists', 'footnotes', 'nl2br', GridTableExtension()]


DOLLAR = re.compile(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)')  # "?" stands for being lazy
DOUBLE_DOLLAR = re.compile(r'(?<!\$)\$\$(?!\$)([\S\s]*?)(?<!\$)\$\$(?!\$)', re.MULTILINE)


def replace_linear_math(match):
    text = f'\\({match.group(1)}\\)'

    return escape_math(text)


def replace_block_math(match):

    # can't include dollars, otherwise they will be also escaped
    return '$$' + escape_math(match.group(1)) + '$$'


def escape_math(text):
    # the problem is that markdown needs escaping to these chars, so we replace user's smth with \smth
    return re.sub(r'[\\\{\}\[\]\$_\*]', lambda match: '\\' + match.group(0), text)


def generate_html(md_text):

    md_text = re.sub(DOLLAR, replace_linear_math, md_text)
    md_text = re.sub(DOUBLE_DOLLAR, replace_block_math, md_text)

    print(md_text)
    md_text = markdown.markdown(md_text, extensions=markdown_extensions)
    print(md_text)
    return Template(md_text).render(Context({}))


class Announcement(models.Model):

    sender = models.ForeignKey(EmailUser, on_delete=models.CASCADE, related_name='sent_announcements')
    receivers = models.ManyToManyField(EmailUser, related_name='recieved_announcements')

    text = models.TextField()

    @property
    def html(self):
        return generate_html(self.text)


# when "pages" file will exist, it should be moved there

class MarkdownPage(models.Model):

    text = models.TextField()

    @property
    def html(self):
        return generate_html(self.text)
