from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    """
        Model for user profiles.

        This class represents a user profile model, containing additional information about the user
        It inherits common user-related fields and methods from models.Model.

        Attributes:
            image (ImageField): Field to store the user's profile image.
            user (OneToOneField): Relationship to the user model using a OneToOneField.
            email (EmailField): The email address of the user.
            phone_number (CharField): The phone number of the user.
            full_name (CharField): The full name of the user.
            create_time (DateTimeField): The timestamp indicating the creation time of the user record.
            update_time (DateTimeField): The timestamp indicating the last update time of the user record.
            is_deleted (BooleanField): Flag indicating whether the user has been deleted or not.

        Meta:
            ordering (list): Specifies the default ordering of profile records, in this case, by username.
            verbose_name (str): Singular name for the model used in the admin interface.
            verbose_name_plural (str): Plural name for the model used in the admin interface.

        Methods:
            get_absolute_url: Method to return the absolute URL of the profile instance.
        """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    update_time = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['-update_time']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"ID: {self.id} full name: {self.full_name}"

    def get_absolute_url(self):
        """Method to return the absolute URL of the profile instance."""
        return reverse("profile_detail", args=[self.id])

    @property
    def capitalize(self):
        """Property method that returns the full name of the user with each word capitalized."""
        return self.full_name.title()
