from django.db import models

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
    
    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")
