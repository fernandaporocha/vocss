from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileInline (admin.StackedInline):
    model = UserProfile
    max_num = 1
    fieldsets = (
        (None, {
            'fields': ('nome', 'dob')
        }),
        (_('Contact information'), {
            'fields': ('email', 'phone', 'mobile')
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
            'fields': ('username', 'first_name', 'last_name', 'password', 'is_active', 'groups')
        }),
    )
    list_display=('dob', 'phone', 'mobile', 'email', 'address', 'city', 'state')
    inlines = (UserProfileInline,)

    def dob (self, instance):
        return instance.profile.dob
    dob.short_description = _("dob")

    def phone (self, instance):
        return instance.profile.phone
    phone.short_description = _("phone")

    def mobile (self, instance):
        return instance.profile.mobile
    mobile.short_description = _("mobile")

    def address (self, instance):
        return instance.profile.address
    address.short_description = _("address")

    def city (self, instance):
        return instance.profile.city
    city.short_description = _("city")

    def state (self, instance):
        return instance.profile.state
    state.short_description = _("state")
    


# Register your models here.
admin.site.unregister (User)
admin.site.register(User, UserProfileAdmin)