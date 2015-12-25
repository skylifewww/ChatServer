from __future__ import unicode_literals

from django.db import models
from accounts.models import UserProfile
from django.utils import timezone

# Create your models here.


class MessageManager(models.Manager):
    def mark_viewed(self, ids):
        """
        Mark messages as viewed and add received time to each message.
        :param ids: message ids to be marked as viewed
        :return: None
        """
        # self.model.objects.filter(id__in=ids).\
        #     update(received_at=timezone.now(), is_viewed=True)
        messages = self.model.objects.filter(id__in=ids)
        for each in messages:
            each.received_at = timezone.now()
            each.is_viewed = True
            each.save()


class Message(models.Model):
    sent_by = models.ForeignKey('accounts.UserProfile', related_name='from_user')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    received_by = models.ForeignKey('accounts.UserProfile', related_name='to_user', default=None)
    is_viewed = models.BooleanField(default=False)
    received_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = MessageManager()

