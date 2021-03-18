from django.contrib import admin
from .models import Unity, Course

class UnityAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'responsible', 'phone', 'email', 'address', 'city', 'state', 'is_active')
        }),
    )

class CourseAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'is_active')
        }),
    )

# Register your models here.
admin.site.register(Unity, UnityAdmin)
admin.site.register(Course, CourseAdmin)