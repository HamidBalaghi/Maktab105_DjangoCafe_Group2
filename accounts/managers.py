<<<<<<< HEAD
# from django.contrib.auth.models import BaseUserManager
#
#
# class UserManager(BaseUserManager):
#     """
#     Custom user manager class for creating users with different permissions.
#     """
#     def create_user(self, phone_number, email, password):
#         """
#         Creates and saves a regular user with the given phone number, email, and password.
#         """
#         if not phone_number:
#             raise ValueError('The phone number must be set')
#         elif not email:
#             raise ValueError('The Email must be set')
#         user = self.model(phone_number=phone_number, email=self.normalize_email(email))
#         user.is_admin = False
#         user.is_staff = False
#         user.is_superuser = False
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_admin(self, phone_number, email, password):
#         """
#         Creates and saves an admin user with the given phone number, email, and password.
#         """
#         user = self.create_user(phone_number, email, password)
#         user.is_staff = True
#         user.is_admin = True
#         user.is_superuser = False
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, phone_number, email, password):
#         """
#         Creates and saves a superuser with the given phone number, email, and password.
#         """
#         user = self.create_user(phone_number, email, password)
#         user.is_superuser = True
#         user.is_admin = True
#         user.is_staff = True
#         user.set_password(password)
#         user.save()
#         return user
=======
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password):
        if not phone_number:
            raise ValueError("The phone number must be set")
        elif not email:
            raise ValueError("The Email must be set")
        user = self.model(phone_number=phone_number, email=self.normalize_email(email))
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user

    def create_admin(self, phone_number, email, password):
        user = self.create_user(phone_number, email, password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, email, password):
        user = self.create_user(phone_number, email, password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user
>>>>>>> 4ba5682ff687a5ad21669e106d07234a7f5114cc
