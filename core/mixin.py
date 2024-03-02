from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager


class BaseModelUserMixin(AbstractBaseUser, PermissionsMixin):
    """
        Base mixin class for user models.

        This class provides common fields and methods for user models. It extends Django's built-in
        AbstractBaseUser and PermissionsMixin classes to provide user authentication and permission
        management functionalities.
    """
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    update_time = models.DateTimeField(auto_now=True, editable=False)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    class Meta:
        abstract = True
        ordering = ['-update_time', 'is_active']
        verbose_name = 'user'
        verbose_name_plural = 'users'

