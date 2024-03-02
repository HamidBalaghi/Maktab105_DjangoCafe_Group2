from django.contrib import admin
from accounts.models import User, Profile
# from .forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, Group
#
#
# class UserAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     model = User
#     list_display = ('email', 'phone_number', 'is_admin', 'is_superuser', 'is_staff', 'is_active')
#     list_filter = ('is_admin', 'is_active')
#     fieldsets = (
#         ('Change personal info', {'fields': ('email', 'phone_number', 'password')}),
#         ('Permissions',
#          {'fields': ('is_superuser', 'is_active', 'is_admin', 'is_staff', 'is_deleted', 'create_time', 'update_time',
#                      'last_login', 'user_groups', 'user_permissions_set')}),
#     )
#
#     add_fieldsets = (
#         ('Creation User', {
#             'fields': ('email', 'phone_number', 'password1', 'password2')}
#          ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ('user_groups', 'user_permissions_set')
#
#
admin.site.register((Profile, User))
# admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)
