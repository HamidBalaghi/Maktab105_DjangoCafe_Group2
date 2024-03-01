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

    def has_perm(self, perm, obj=None):
        """Method to check if the user has a specific permission."""
        return True

    def has_module_perms(self, app_label):
        """Method to check if the user has permissions for a specific module."""
        return True


class SoftDeleteMixin(models.QuerySet):
    def delete(self):
        """
        Soft delete objects in the queryset.

        Instead of permanently deleting objects from the database,
        mark them as deleted by setting the 'is_deleted' field to True.
        """
        return super().update(is_deleted=True, is_active=False)


class DeleteManagerMixin(models.Manager):

    def get_queryset_object(self):
        """
        Get the queryset object associated with this manager.

        If the queryset object has not been created yet, create it
        using ManagerQuerySetDelete to handle soft deletion.
        """
        if not hasattr(self.__class__, '__queryset'):
            self.__class__.__queryset = SoftDeleteMixin(self.model)
        return self.__queryset

    def get_queryset(self):
        """
        Get the filtered queryset, excluding deleted and inactive objects.

        This method filters out objects marked as deleted ('is_deleted'=True)
        and inactive ('is_active'=False) from the queryset.
        """
        return self.get_queryset_object().filter(is_active=True, is_deleted=False)

    def archive(self):
        """
        Retrieve all objects, including deleted and inactive ones.

        This method returns all objects in the queryset, including those
        marked as deleted or inactive. It is provided as an alias for
        get_queryset() but may be redundant in most use cases.
        """
        return super().get_queryset()
