from __future__ import unicode_literals

from django.db import models
from accounts.models import UserProfile
from django.utils import timezone

# Create your models here.


class MessageManager(models.Manager):
    def get_messages(self, user_id):
        return


class Message(models.Model):
    sent_by = models.ForeignKey('accounts.UserProfile', related_name='from_user')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    received_by = models.ForeignKey('accounts.UserProfile', related_name='to_user')
    is_viewed = models.BooleanField(default=False)
    received_at = models.DateTimeField(default=None, null=True, blank=True)


