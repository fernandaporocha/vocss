from django.db import models
import datetime

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Unity (models.Model):
    name = models.CharField(_("name"), max_length=100, blank=False, null=False)
    responsible = models.CharField(_("responsible"), max_length=100, blank=True, null=False)
    phone = models.CharField(_("phone"), max_length=100, blank=True, null=False)
    email = models.CharField(_("email"), max_length=100, blank=True, null=False)
    address = models.CharField(_("address"), max_length=100, blank=True, null=False)
    city = models.CharField(_("city"), max_length=50, blank=True, null=False)
    state = models.CharField(_("state"), max_length=50, blank=True, null=False)
    is_active = models.BooleanField (_("is active?"), default=True)

    class Meta:
        verbose_name = _("unity")
        verbose_name_plural = _("unities")

class Course (models.Model):
    name = models.CharField(_("name"), max_length=100, blank=False, null=False)
    is_active = models.BooleanField (_("is active?"), default=True)

    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")

class Student(models.Model):
    YEAR_CHOICES = []
    for r in range(2009, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    SEX = (('m', _('Male')), ('f', _('Female')))
    ETHINICITY = (('w', _('White')), ('n', _('Black')), ('h', _('hispanic')),('a', _('asian')),('i', _('indian')),('n', _('non declared')))
    STUDY_PERIOD = (('m', _('Morning')), ('a', _('afternoon')), ('e', _('evening')), ('f', _('fulltime')))
    OTHER_COURSE_PERIOD = (('m', _('Morning')), ('a', _('afternoon')), ('e', _('evening')))
    CURRENTLY_YEAR = (('b1', _('berçário 1')), ('b2', _('berçário 2')), ('m1', _('maternal 1')), ('p1', _('pré-escola 1')), ('p2', _('pré-escola 2')), ('f1', _('1º Ano (Fundamental)')), ('f2', _('2º Ano (Fundamental)')), ('f3', _('3º Ano (Fundamental)')), ('f4', _('4º Ano (Fundamental)')), ('f5', _('5º Ano (Fundamental)')), ('f6', _('6º Ano (Fundamental)')), ('f7', _('7º Ano (Fundamental)')), ('f8', _('8º Ano (Fundamental)')), ('f9', _('9º Ano (Fundamental)')), ('m1', _('1º Ano (Médio)')), ('m2', _('2º Ano (Médio)')), ('m3', _('3º Ano Médio')))

    year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    name = models.CharField(_("name"), max_length=100, blank=False, null=False)
    shortname = models.CharField(_("shortname"), max_length=100, blank=False, null=False)
    mobile = models.CharField(_("mobile"), max_length=100, blank=True, null=False)
    sex = models.CharField (_("sex"), max_length=1, choices=SEX, blank=True, null=False)
    ethinicity = models.CharField (_("ethinicity"), max_length=1, choices=ETHINICITY, blank=True, null=False)
    dob = models.DateField(_("dob"), auto_now=False, blank=True, null=True)
    orign_state = models.CharField(_("state of orign"), max_length=50, blank=True, null=False)
    orign_city = models.CharField(_("city of orign"), max_length=50, blank=True, null=False)
    cpf = models.CharField(_("cpf"), max_length=100, blank=False, null=False)
    rg = models.CharField(_("rg"), max_length=100, blank=False, null=False)
    issuing_body = models.CharField(_("issuing body"), max_length=100, blank=False, null=False)
    birth_certificate = models.CharField(_("birth certificate"), max_length=100, blank=False, null=False)
    book = models.CharField(_("book"), max_length=100, blank=False, null=False)
    page = models.CharField(_("page"), max_length=100, blank=False, null=False)
    photo = models.ImageField (_('photo'), upload_to='user/photos/', blank=True, null=False)
    address = models.CharField(_("address"), max_length=100, blank=True, null=True)
    county = models.CharField(_("county"), max_length=100, blank=True, null=True)
    city = models.CharField(_("city"), max_length=50, blank=True, null=True)
    state = models.CharField(_("state"), max_length=50, blank=True, null=True)
    postal_code = models.CharField(_("postal code"), max_length=50, blank=True, null=True)
    school_name = models.CharField(_("school name"), max_length=50, blank=True, null=True)
    study_period = models.CharField (_("study period"), max_length=1, choices=STUDY_PERIOD, blank=True, null=False)
    currently_year = models.CharField (_("currently year"), max_length=2, choices=CURRENTLY_YEAR, blank=True, null=False)
    do_other_courses = models.BooleanField (_("does the student do other courses?"), default=False)
    extra_courses = models.CharField(_("which courses?"), max_length=50, blank=True, null=True)
    special_need = models.CharField(_("does the student have any special need?"), max_length=50, blank=True, null=True)
    top_size = models.CharField(_("top size"), max_length=50, blank=True, null=True)
    bottom_size = models.CharField(_("bottom size"), max_length=50, blank=True, null=True)
    shoes_size = models.CharField(_("shoes size"), max_length=50, blank=True, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")
    

class Responsible (models.Model):
    DEGREE_OF_RELATIONSHIP = (('f', _('Father')), ('m', _('Mother')), ('u', _('Uncle/Aunt')), ('g', _('Grandfather/Grandmother')), ('o', _('Other')))
    name = models.CharField(_("name"), max_length=100, blank=False, null=False)
    degree_of_relationship =  models.CharField (_("degree od relationship"), max_length=1, choices=DEGREE_OF_RELATIONSHIP, blank=True, null=False)
    dob = models.DateField(_("dob"), auto_now=False, blank=True, null=True)
    cpf = models.CharField(_("cpf"), max_length=100, blank=False, null=True)
    rg = models.CharField(_("rg"), max_length=100, blank=False, null=True)
    mobile = models.CharField(_("mobile"), max_length=100, blank=True, null=True)
    email = models.CharField(_("email"), max_length=100, blank=True, null=True)
    live_with_the_student = models.BooleanField (_("Live with the student?"), default=True)
    address = models.CharField(_("address"), max_length=100, blank=True, null=True)
    city = models.CharField(_("city"), max_length=50, blank=True, null=True)
    state = models.CharField(_("state"), max_length=50, blank=True, null=True)
    postal_code = models.CharField(_("postal code"), max_length=50, blank=True, null=True)
    curriculum = models.FileField (_('curriculum'), upload_to='documents/responsible/curriculum/', blank=True, null=False)
    student = models.ForeignKey(Student, verbose_name=_("student"), on_delete=models.DO_NOTHING, null=True) 
    EDUCATION_LEVEL = (('fi', _('Fundamental Incompleto')), ('fc', _('Fundamental Completo')),('mi', _('Médio Incompleto')), ('mc', _('Médio Completo')),('si', _('Superior Incompleto')), ('sc', _('Superior Completo')),('pi', _('Pós Graduação Incompleta')), ('pc', _('Pós Graduação Completa')))
    FAMILY_INCOME = (('1', _('Até 1 salário mínimo (até R$1.100,00)')), ('2', _('Até 2 salários mínimos (de R$1.100,01 a R$2.200,00)')),('3', _('Até 3 salários mínimos (de R$2.200,01 a R$3.300,00)')), ('4', _('Mais de 3 salários mínimos')))
    education_level = models.CharField (_("education level"), max_length=2, choices=EDUCATION_LEVEL, blank=True, null=False)
    is_working = models.BooleanField (_("is currently working?"), default=True)
    profession = models.CharField(_("profession"), max_length=100, blank=True, null=True)
    family_income = models.CharField (_("family income"), max_length=1, choices=FAMILY_INCOME, blank=True, null=True)
    student_helps_income = models.BooleanField (_("does the student help with the family income?"), default=False)
    receive_government_benefit = models.BooleanField (_("does the family receive any government benefit?"), default=False)
    received_benefits = models.CharField(_("received benefits"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("responsible")
        verbose_name_plural = _("responsibles")
