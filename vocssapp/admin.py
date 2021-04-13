from django.contrib import admin
from .models import Unity, Course, Responsible, Student, Class

from django.utils.translation import ugettext_lazy as _

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

class ResponsibleInline (admin.StackedInline):
    fieldsets = (
        (None, {
            'fields': ('name', 'degree_of_relationship', 'dob', 'cpf', 'rg', 'mobile', 'email', 'live_with_the_student', 'address', 'city', 'state', 'postal_code', 'curriculum')
        }),
        (_("socio economic information"), {
            'fields': ('education_level', 'is_working', 'profession', 'family_income', 'student_helps_income', 'receive_government_benefit', 'received_benefits')
        }),
    )
    model = Responsible
    max_num = 1
    verbose_name = _('responsible')
    verbose_name_plural = _('responsibles')

class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("student information"), {
            'fields': ('year', 'name', 'shortname', 'mobile', 'sex', 'ethinicity', 'dob', 'orign_state', 'orign_city', 'cpf', 'rg', 'issuing_body', 'birth_certificate', 'book', 'page', 'photo')
        }),
        (_("student address"), {
            'fields': ('address', 'county', 'city', 'state', 'postal_code')
        }),
        (_("school information"), {
            'fields': ('school_name', 'study_period', 'currently_year', 'do_other_courses', 'extra_courses')
        }),
        (_("additional  information"), {
            'fields': ('special_need', 'top_size', 'bottom_size', 'shoes_size')
        }),
    )
    class Media:
        css = {
            'all': ('css/responsible_no_heading.css', )     # Include extra css
        }
    inlines = (ResponsibleInline,)
    verbose_name = _('student')
    verbose_name_plural = _('students')

class ClassAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'course', 'teacher', 'num_places', 'start_date', 'end_date', 'students')
        }),
    )

# Register your models here.
admin.site.register(Unity, UnityAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)