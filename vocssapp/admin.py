from django.contrib import admin
from .models import Unity

class UnityAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'responsible', 'phone', 'email', 'address', 'city', 'state')
        }),
    )

# Register your models here.
admin.site.register(Unity, UnityAdmin)