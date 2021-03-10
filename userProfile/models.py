from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserProfile (models.Model):
    user = models.OneToOneField('auth.User', verbose_name=_("user"), on_delete=models.CASCADE)
    nome = models.CharField(_("name"), max_length=100, blank=False, null=False)
    dob = models.DateField(_("dob"), auto_now=False, blank=True, null=True)
    phone = models.CharField(_("phone"), max_length=100, blank=True, null=False)
    mobile = models.CharField(_("mobile"), max_length=100, blank=True, null=False)
    email = models.CharField(_("email"), max_length=100, blank=True, null=False)
    address = models.CharField(_("address"), max_length=100, blank=True, null=False)
    city = models.CharField(_("city"), max_length=50, blank=True, null=False)
    state = models.CharField(_("state"), max_length=50, blank=True, null=False)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])