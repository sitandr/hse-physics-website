from django.db import models
from . import EmailUser
import markdown
from django.template import Template, Context
import re


markdown_extensions = ['tables', 'sane_lists', 'footnotes', 'nl2br', 'pymdownx.arithmatex']

DOLLAR_REPLACER = re.compile(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)')  # "?" stands for being lazy


def generate_html(md_text):
    md_text = md_text.replace(r'\\', r'\\\\')
    # the problem is that markdown also uses \ as escaping, so we replace user's \\ with \\\\

    md_text = re.sub(DOLLAR_REPLACER, r'\\\\( \g<1> \\\\)', md_text)

    print(md_text)

    return Template(markdown.markdown(md_text, extensions=markdown_extensions)).render(Context({}))


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
