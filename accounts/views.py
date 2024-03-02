from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

# from .models import Profile, User
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'profile/login.html'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'You have already login successfully', extra_tags='success')
            return redirect('login')
        else:
            return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LoginRequiredMixin, View):
    http_method_names = ['get']
    success_url = reverse_lazy('product_home')

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
