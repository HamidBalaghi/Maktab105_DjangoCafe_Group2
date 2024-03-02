from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager


class BaseModelUserMixin(AbstractUser):
    """
        Base mixin class for user models.

        This class provides common fields and methods for user models. It extends Django's built-in
        AbstractBaseUser and PermissionsMixin classes to provide user authentication and permission
        management functionalities.
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    update_time = models.DateTimeField(auto_now=True, editable=False)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username', 'email']
    objects = UserManager()

    class Meta:
        abstract = True
        ordering = ['-update_time']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def has_perm(self, perm, obj=None):
        """Method to check if the user has a specific permission."""
        return True

    def has_module_perms(self, app_label):
        """Method to check if the user has permissions for a specific module."""
        return True

    @property
    def groups(self):
        return self.user_groups

    @property
    def user_permissions(self):
        return self.user_permissions_set
