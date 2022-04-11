from django.db import models
from . import EmailUser


class Announcement(models.Model):

    sender = models.ForeignKey(EmailUser, on_delete=models.CASCADE, related_name='sent_announcements')
    receivers = models.ManyToManyField(EmailUser, related_name='recieved_announcements')

    text = models.TextField()
