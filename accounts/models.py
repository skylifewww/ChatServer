from __future__ import unicode_literals

import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          is_active=False,
                          last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self._create_user(username, email, password, False, **extra_fields)
        user.is_active = True
        user.save()


class UserProfile(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=30, unique=True,
                                validators=[
                                    validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=1000, default='')
    last_name = models.CharField(max_length=1000, default='')
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_seen_at = models.DateTimeField(default=None, null=True, blank=True)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['first_name', 'last_name']

    def get_short_name(self):
        name = self.username
        return name.strip()

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def initials(self):
        return '%s%s' % (self.first_name[0], self.last_name[0])

