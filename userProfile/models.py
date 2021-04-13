from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from vocssapp.models import Document

class ExtraField (models.Model):
    name = models.CharField (_("name"), max_length=100)
    user = models.ManyToManyField ('auth.User', verbose_name=_("users"), through='ExtraFieldData')

    def __unicode__ (self):
        return self.name

    class Meta:
        verbose_name = _("extra field")
        verbose_name_plural = _("extra fields")

class ExtraFieldData (models.Model):
    user = models.ForeignKey ('auth.User', verbose_name=_("user"), on_delete=models.DO_NOTHING)
    extrafield = models.ForeignKey ('ExtraField', verbose_name=_("extra field"), on_delete=models.DO_NOTHING)
    data = models.CharField (_("data"), max_length=1000)

    def __unicode__ (self):
        return self.extrafield.name

    class Meta:
        verbose_name = _("extra field data")
        verbose_name_plural = _("extra fields data")

# Create your models here.
class UserProfile (models.Model):    
    SEX = (('m', _('Male')), ('f', _('Female')))
    ETHINICITY = (('w', _('White')), ('n', _('Black')), ('h', _('hispanic')))

    sex = models.CharField (_("sex"), max_length=1, choices=SEX, blank=True, null=False)
    ethinicity = models.CharField (_("ethinicity"), max_length=1, choices=ETHINICITY, blank=True, null=False)

    user = models.OneToOneField('auth.User', verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=100, blank=False, null=False)
    dob = models.DateField(_("dob"), auto_now=False, blank=True, null=True)
    phone = models.CharField(_("phone"), max_length=100, blank=True, null=False)
    mobile = models.CharField(_("mobile"), max_length=100, blank=True, null=False)
    address = models.CharField(_("address"), max_length=100, blank=True, null=False)
    county = models.CharField(_("county"), max_length=100, blank=True, null=False)
    city = models.CharField(_("city"), max_length=50, blank=True, null=False)
    state = models.CharField(_("state"), max_length=50, blank=True, null=False)
    postal_code = models.CharField(_("postal code"), max_length=50, blank=True, null=False)
    photo = models.ImageField (_('photo'), upload_to='user/photos/', blank=True, null=False)
    curriculum = models.FileField (_('curriculum'), upload_to='documents/users/curriculum/', blank=True, null=False)
    rg = models.FileField (_('rg'), upload_to='documents/rg/', blank=True, null=False)
    cpf = models.FileField (_('cpf'), upload_to='documents/cpf/', blank=True, null=False)
    documents = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)
    #documents = models.CharField(_("state"), max_length=50, blank=True, null=False)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")



User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])