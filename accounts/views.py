from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from .forms import EditProfileForm, UserRegistrationForm, UserCreationForm, ProfileForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from .models import Profile


class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        return render(request, self.template_name)


class UserLoginView(LoginView):
    template_name = 'profile/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'You have already login successfully', extra_tags='success')
            return redirect('home')
        else:
            return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LoginRequiredMixin, View):
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request, 'You have already logged out successfully', extra_tags='success')
            return redirect('home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(self.request)
        messages.success(request, 'Logout successfully', extra_tags='success')
        return redirect('home')


class EditeUserView(LoginRequiredMixin, View):
    form_class = EditProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user.profile, initial={'email': request.user.email})
        return render(request, 'profile/chage_profile.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data.get('email')
            request.user.save()
            messages.success(request, 'Your profile has been updated successfully', extra_tags='success')
            return redirect('home')
        else:
            messages.error(request, 'Your profile has not been updated successfully', extra_tags='error')
            return redirect('edit_user')


class CreateUserView(View):
    form_class = UserRegistrationForm
    template_name = 'profile/create_user.html'

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


class CreateProfileView(View):
    template_name = 'profile/create_profile.html'

    def get(self, request):
        form = ProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')  # Redirect to a success page
        return render(request, self.template_name, {'form': form})


class ChangePasswordView(PasswordChangeView):
    form_class = UserCreationForm
    template_name = 'profile/chage_password.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class RegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'

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
            return redirect('registration_success')
        return render(request, self.template_name, {'form': form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        profile_get_object = Profile.objects.get(user=self.request.user)
        return get_object_or_404(User, pk=self.kwargs['pk']) and profile_get_object
