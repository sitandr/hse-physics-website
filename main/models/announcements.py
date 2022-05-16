from django.db import models
from . import EmailUser
import markdown
from django.template import Template, Context


class Announcement(models.Model):

    sender = models.ForeignKey(EmailUser, on_delete=models.CASCADE, related_name='sent_announcements')
    receivers = models.ManyToManyField(EmailUser, related_name='recieved_announcements')

    text = models.TextField()

    @property
    def html(self):
        return Template(markdown.markdown(self.text)).render(Context({}))
