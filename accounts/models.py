from django.db import models
from core.mixin import BaseModelUserMixin
from django.urls import reverse


class User(BaseModelUserMixin):
    """
        Model for users.

        This class represents a user in the system. It extends the BaseModelUserMixin to inherit common fields
        and methods related to user management.

        Attributes:
            email (EmailField): The email address of the user.
            phone_number (CharField): The phone number of the user.
            full_name (CharField): The full name of the user.
            create_time (DateTimeField): The timestamp indicating the creation time of the user record.
            update_time (DateTimeField): The timestamp indicating the last update time of the user record.
            is_deleted (BooleanField): Flag indicating whether the user has been deleted or not.
            is_active (BooleanField): Flag indicating whether the user is active or not.
            is_admin (BooleanField): Flag indicating whether the user has admin privileges.
            is_staff (BooleanField): Flag indicating whether the user is staff or not.
            is_superuser (BooleanField): Flag indicating whether the user is a superuser or not.
            USERNAME_FIELD (str): Field used for authentication, in this case, the phone number.
            REQUIRED_FIELDS (list): List of fields required for creating a user, in this case, email and full name.
            objects (UserManager): Custom manager for handling user queries.

        Methods:
            has_perm: Method to check if the user has a specific permission.
            has_module_perms: Method to check if the user has permissions for a specific module.
            capitalize: Property method that returns the full name of the user with each word capitalized.
        """




class Profile(BaseModelUserMixin):
    """
        Model for user profiles.

        This class represents a user profile model, containing additional information about the user
        such as their image and associated basket. It inherits common user-related fields and methods
        from BaseModelUserMixin.

        Attributes:
            image (ImageField): Field to store the user's profile image.
            basket (OneToOneField): Relationship to the user's basket using a OneToOneField.
            user (OneToOneField): Relationship to the user model using a OneToOneField.
            email (EmailField): The email address of the user.
            phone_number (CharField): The phone number of the user.
            full_name (CharField): The full name of the user.
            create_time (DateTimeField): The timestamp indicating the creation time of the user record.
            update_time (DateTimeField): The timestamp indicating the last update time of the user record.
            is_deleted (BooleanField): Flag indicating whether the user has been deleted or not.
            is_active (BooleanField): Flag indicating whether the user is active or not.
            is_admin (BooleanField): Flag indicating whether the user has admin privileges.
            is_staff (BooleanField): Flag indicating whether the user is staff or not.
            is_superuser (BooleanField): Flag indicating whether the user is a superuser or not.
            USERNAME_FIELD (str): Field used for authentication, in this case, the phone number.
            REQUIRED_FIELDS (list): List of fields required for creating a user, in this case, email and full name.
            objects (UserManager): Custom manager for handling user queries.

        Meta:
            ordering (list): Specifies the default ordering of profile records, in this case, by username.
            verbose_name (str): Singular name for the model used in the admin interface.
            verbose_name_plural (str): Plural name for the model used in the admin interface.

        Methods:
            get_absolute_url: Method to return the absolute URL of the profile instance.
            has_perm: Method to check if the user has a specific permission.
            has_module_perms: Method to check if the user has permissions for a specific module.
        """
    image = models.ImageField(upload_to='images/profile/%Y/%m/%d/')
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE, related_name='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def get_absolute_url(self):
        """Method to return the absolute URL of the profile instance."""
        return reverse("profile_detail", args=[self.id])