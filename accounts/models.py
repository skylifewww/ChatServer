from __future__ import unicode_literals

import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        """
        Add user in the table. Following are the fields needed.
        :param username: required
        :param email: required
        :param password: required
        :param is_staff: optional
        :param is_superuser: optional
        :param extra_fields: optional
        :return: created user
        """
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self._create_user(username, email, password, is_staff=False, is_superuser=False, **extra_fields)
        user.is_active = True
        user.last_seen_at = timezone.now()
        user.save()

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, is_staff=True, is_superuser=True, **extra_fields)
        user.is_active = True
        user.last_seen_at = timezone.now()
        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=30, unique=True,
                                validators=[
                                    validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=1000, default='')
    last_name = models.CharField(max_length=1000, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_seen_at = models.DateTimeField(default=None, null=True, blank=True)

    objects = UserProfileManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

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

