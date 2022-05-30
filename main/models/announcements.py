from django.db import models
from . import EmailUser
from ..other.markdown import generate_html


class Announcement(models.Model):

    sender = models.ForeignKey(EmailUser, on_delete=models.CASCADE, related_name='sent_announcements')
    receivers = models.ManyToManyField(EmailUser, related_name='recieved_announcements')
    name = models.CharField(max_length=30)
    text = models.TextField()

    @property
    def html(self):
        return generate_html('# ' + self.name + '\n' + self.text)

    class Meta:
        ordering = ['-id']
