from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from utils.roles import *


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _check_username(self, username=''):
        # black_list = ('user', 'admin', 'username', 'administrator', 'unknown', )
        black_list = ()
        response = {
            "access": False,
            "username": username,
            "message": ""
        }

        # Check for Username length
        if len(username) < 4:
            response.update({"message": "Username length must be more than 4"})
            return response

        # Check for Username black list
        for item in black_list:
            if item == username:
                response.update({"message": "Username not allowed"})
                return response

        response.update({"access": True})
        return response

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        check = self._check_username(username)

        if check.get("access"):
            user = self.model(username=check.get("username"), **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        else:
            print(check.get("message"))
            return None

    def create_user(self, username, password=None, **extra_fields):
        print(username)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=32)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)

    role = models.SmallIntegerField(choices=ROLES, default=Guest)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')
