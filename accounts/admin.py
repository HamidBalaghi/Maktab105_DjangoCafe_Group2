from django.contrib import admin
from accounts.models import User, Profile
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = ('email', 'phone_number', 'is_admin', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        ('Change personal info', {'fields': ('email', 'phone_number', 'password')}),
        ('Permissions',
         {'fields': ('is_superuser', 'is_active', 'is_admin', 'is_staff', 'is_deleted', 'update_time',
                     'last_login', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        ('Creation User', {
            'fields': ('email', 'phone_number', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('creat_time', 'update_time', 'last_login')

        return self.readonly_fields


admin.site.register(Profile)
admin.site.register(User, UserAdmin)
