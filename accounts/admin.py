from django.contrib import admin
from accounts.models import  Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class ExtendedUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ExtendedUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
admin.site.register(Profile)
