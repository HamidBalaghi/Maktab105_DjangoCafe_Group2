from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import User
from django import forms
from .models import Profile


class EditProfileForm(forms.ModelForm):
    """
    Form for editing user profile details.
    """
    email = forms.EmailField(label='Email', max_length=254)

    class Meta:
        model = Profile
        fields = ('phone_number', 'full_name')


class UserCreationForm(PasswordChangeForm):
    """
    Custom form for user creation, inheriting from PasswordChangeForm.
    """

    def __init__(self, user, *args, **kwargs):
        """
        Initializes the form instance with the user object.
        """
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


class ProfileForm(forms.ModelForm):
    """
    Form for updating profile details.
    """

    class Meta:
        model = Profile
        fields = ['phone_number', 'full_name']


class UserRegistrationForm(forms.Form):
    """
    Form for user registration.
    """
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', max_length=150)
    last_name = forms.CharField(label='Last Name', max_length=150)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        """
        Validates the uniqueness of the username.
        """
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        """
        Validates the uniqueness of the email address.
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

    def clean(self):
        """
        Validates that the two password fields match.
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
