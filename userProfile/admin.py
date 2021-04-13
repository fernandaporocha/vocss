from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import ExtraFieldData
from vocssapp.models import Document
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
  UserCreationForm,
)

class ExtraFieldInline (admin.TabularInline):
    model = ExtraFieldData
    extra = 0
    verbose_name = _('extra field data')
    verbose_name_plural = _('extra fields data')
    #form = ExtraFieldAdminForm

class DocumentInline (admin.TabularInline):
    model = Document
    fieldsets = (
        (None, {
            'fields': ('name', 'file')
        }),
    )
    verbose_name = _('document')
    verbose_name_plural = _('documents')

class UserProfileInline (admin.StackedInline):
    model = UserProfile
    max_num = 1
    fieldsets = (
        (None, {
            'fields': ('name', 'dob', 'sex', 'ethinicity', 'phone', 'mobile')
        }),
        (_('Addr'), {
            'fields': ('address', 'county', 'city', 'state', 'postal_code')
        }),
        (_('attachment'), {
            'fields': ('photo', 'rg', 'cpf', 'curriculum', 'documents')
        }),
    )
    inlines = (ExtraFieldInline,)
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