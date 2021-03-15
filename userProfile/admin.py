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
            'fields': ('nome', 'dob')
        }),
        (_('Contact information'), {
            'fields': ('phone', 'mobile')
        }),
        (_('Addr'), {
            'fields': ('address', 'city', 'state')
        }),
    )
    verbose_name = _('profile')
    verbose_name_plural = _('profile')

class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'username',
        }

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    class Meta:
        model = User
        #fields = ("username", "email")
        fields = '__all__'
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'is_active', 'groups')
        }),
    )
    list_display=('username', 'name', 'phone', 'mobile')
    add_form = CustomUserCreationForm
    
    class Media:
        css = {
            'all': ('css/userprofile_no_heading.css', )     # Include extra css
        }
    inlines = (UserProfileInline,)

    def name (self, instance):
        return instance.profile.nome
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