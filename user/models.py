from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import RecuritManager

# Create your models here.
class Recruit(AbstractBaseUser, PermissionsMixin):
    code = models.CharField(max_length=50, unique=True, db_index=True, null=False)

    rank = models.CharField(verbose_name=_("Rank"), max_length=255, null=True, blank=True)
    name = models.CharField(default="", max_length=255)
    arm = models.CharField(verbose_name=_("Arm"), max_length=255, null=True, blank=True)
    blood_type = models.CharField(verbose_name=_("Blood Type"), max_length=255, null=True, blank=True)
    unit = models.CharField(verbose_name=_("Unit"), max_length=255, null=True, blank=True)
    current_job = models.CharField(verbose_name=_("current_job"), max_length=255, null=True, blank=True)
    college = models.CharField(verbose_name=_("college"), max_length=255, null=True, blank=True)
    home_phone = models.CharField(verbose_name=_("home_phone"), max_length=255, null=True, blank=True)
    email_address = models.CharField(verbose_name=_("email_address"), max_length=255, null=True, blank=True)
    number_of_current_spouses = models.IntegerField(verbose_name=_("number_of_current_spouses"), default=0)
    number_of_children = models.IntegerField(verbose_name=_("number_of_children"), default=0)
    men = models.IntegerField(verbose_name=_("Men"), default=0)
    women = models.IntegerField(verbose_name=_("Women"), default=0)
    spouse_date = models.DateField(verbose_name=_("spouce_date"), null=True, blank=True)
    number_of_past_spouses = models.IntegerField(verbose_name=_("number_of_past_spouces"), default=0)
    date_of_break_up = models.DateField(verbose_name=_("date of break up"), null=True, blank=True)
    
    religion = models.CharField(verbose_name=_("Religion"), max_length=255, blank=True, null=True)
    national_number = models.CharField(max_length=14, verbose_name=_("National Number"), blank=True, null=True)
    date_of_graduation = models.DateField(verbose_name=_("Date of Graduation"), blank=True, null=True)

    education = models.CharField(verbose_name=_("Education"), max_length=255,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    birth_location = models.CharField(default="", max_length=255, blank=True)
    marital_status = models.CharField(default="", max_length=255, blank=True)
    number_of_children = models.PositiveIntegerField(default=0)
    residence = models.CharField(verbose_name=_("Residence"), max_length=255, null=True, blank=True)
    triple_digit = models.CharField(default="", max_length=22, blank=True)
    mobile_number = models.CharField(default="", max_length=255, blank=True)      

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = "code"
    REQUIRED_FIELDS=['name']                                

    objects = RecuritManager()  

    def __str__(self):
        return f"{self.name}"
