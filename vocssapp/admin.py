from django.contrib import admin
from .models import Unity, Course, Responsible, Student, Klass, Lesson, StudentAttendance, Grade, FormalSchool, Absence, School, Subject, Evaluation, BehaviourEvaluation, CognitiveEvaluation

from django.forms import ModelForm
from django.contrib.auth.models import User
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

class KlassAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'course', 'teacher', 'num_places', 'start_date', 'end_date','start_time', 'end_time', 'students', 'extra_information')
        }),
    )

class StudentAttendanceInline (admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': ('student', 'status', 'observation')
        }),
    )
    model = StudentAttendance
    max_num = 0
    can_delete = False

    readonly_fields = ['student', ]


class LessonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('klass', 'date')
        }),
    )
    inlines = (StudentAttendanceInline,)

class GradeInline (admin.TabularInline):
    fieldsets = (
        (None, {
             'fields': ('subject', 'first', 'second', 'third', 'fourth')
        }),
    )
    model = Grade

class AbsenceInline (admin.TabularInline):
    fieldsets = (
        (None, {
             'fields': ('first', 'second', 'third', 'fourth')
        }),
    )
    model = Absence
    max_num = 1
    can_delete = False

class FormalSchoolAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
             'fields': ('student', 'school', 'currently_year')
        }),
    )
    
    list_display=('student', 'school', 'currently_year')
    inlines = (GradeInline,AbsenceInline,)

class SchoolAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
             'fields': ('name',)
        }),
    )
    
class SubjectAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
             'fields': ('name',)
        }),
    )

class BehaviourEvaluationInline (admin.TabularInline):
    fieldsets = (
        (None, {
             'fields': ('date', 'autonomy', 'organization', 'assiduity', 'punctuality', 'dedication', 'mobile_use', 'personal_presentation',)
        }),
    )
    model = BehaviourEvaluation
    extra = 1

class CognitiveEvaluationInline (admin.TabularInline):
    fieldsets = (
        (None, {
             'fields': ('date', 'problem_solving', 'oral_expression', 'traditional_reading', 'music_reading', 'course_performance')
        }),
    )
    model = CognitiveEvaluation
    extra = 1
    
class EvaluationAdmin (admin.ModelAdmin):
    fieldsets = (
        (None, {
             'fields': ('student', 'klass', 'observation',)
        }),
    )
    
    list_display=('student','klass')
    inlines = (BehaviourEvaluationInline, CognitiveEvaluationInline)



# Register your models here.
admin.site.register(Unity, UnityAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Klass, KlassAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(FormalSchool, FormalSchoolAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Evaluation, EvaluationAdmin)