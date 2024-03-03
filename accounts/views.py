from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .forms import EditProfileForm, UserRegistrationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class UserLoginView(LoginView):
    template_name = 'profile/login.html'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'You have already login successfully', extra_tags='success')
            return redirect('/')
        else:
            return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LoginRequiredMixin, View):
    success_url = reverse_lazy('p')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request, 'You have already logged out successfully', extra_tags='success')
            return redirect('/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(self.request)
        messages.success(request, 'Logout successfully', extra_tags='success')
        return redirect('/') or redirect('home')


class EditeUserView(LoginRequiredMixin, View):
    form_class = EditProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user.profile, initial={'email': request.user.email})
        return render(request, 'profile/change_password.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data.get('email')
            request.user.save()
            messages.success(request, 'Your profile has been updated successfully', extra_tags='success')
            return redirect('login', )
        else:
            messages.error(request, 'Your profile has not been updated successfully', extra_tags='error')
            return redirect('edit_user')


class CreateUserView(View):
    form_class = UserRegistrationForm
    template_name = 'profile/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f'Account created for {username}', extra_tags='success')
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


class ChangePasswordView(LoginRequiredMixin, View):
    form_class = UserCreationForm
    template_name = 'change_password.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully', extra_tags='success')
            return redirect('profile_detail')
        else:
            return render(request, self.template_name, {'form': form})
