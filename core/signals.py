from django.contrib.auth.models import User
from django.db.models.signals import post_save
from accounts.models import Profile


def create_profile(sender, **kwargs):
    """Function to create a profile for a new user."""
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(receiver=create_profile, sender=User)
