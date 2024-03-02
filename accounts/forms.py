from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from accounts.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm_password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError("Password don't match")
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="You can change using password <a href=\"../password\">this form</a>")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password', 'last_login')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'email': 'Email',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'email': 'Enter your email',
            'phone_number': 'Enter your phone number',
        }
        error_messages = {
            'email': {
                'required': 'Email is required',
                'invalid': 'Invalid email format',
            },
            'phone_number': {
                'required': 'Phone number is required',
                'invalid': 'Invalid phone number format',
            },
        }


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    phone_number = forms.CharField(label='Phone Number', max_length=11)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email
