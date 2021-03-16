from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
  UserCreationForm,
)
class UserProfileInline (admin.StackedInline):
    model = UserProfile
    max_num = 1
    fieldsets = (
        (None, {
            'fields': ('name', 'dob', 'phone', 'mobile')
        }),
        (_('Addr'), {
            'fields': ('address', 'city', 'state')
        }),
    )
    verbose_name = _('profile')
    verbose_name_plural = _('profile')

class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'is_active', 'groups')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'groups'),
        }),
    )
    list_display=('username', 'name', 'phone', 'mobile', 'email')
    list_filter = ('is_active',)

    
    class Media:
        css = {
            'all': ('css/userprofile_no_heading.css', )     # Include extra css
        }
    inlines = (UserProfileInline,)

    def name (self, instance):
        return instance.profile.name
    name.short_description = _("name")

    def dob (self, instance):
        return instance.profile.dob
    dob.short_description = _("dob")

    def phone (self, instance):
        return instance.profile.phone
    phone.short_description = _("phone")

    def mobile (self, instance):
        return instance.profile.mobile
    mobile.short_description = _("mobile")

# Register your models here.
admin.site.unregister (User)
admin.site.register(User, UserProfileAdmin)