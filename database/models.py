from datetime import date

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from user.models import Recruit

class Parent(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="parents")
    relate = models.CharField(default="", choices=[
        ('الوالد', 'الوالد'),
        ('الوالده', 'الوالده'),
        ('الجد للوالد', 'الجد للوالد'),
        ('الجد للوالدة', 'الجد للوالدة'),
    ], max_length=255, blank=True)
    name = models.CharField(default="", max_length=255, blank=True)
    nationality = models.CharField(default="", max_length=255, blank=True)
    qualification = models.CharField(verbose_name=_("Qualification"), max_length=255, blank=True, default="")
    job = models.CharField(verbose_name=_("Job"), max_length=255, default="", blank=True)
    military_officer = models.BooleanField(default=False)
    residence = models.CharField(verbose_name=_("Residence"), max_length=255, default="", blank=True)  

    def __str__(self):
        return f"{self.name}"
    
class Supports(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="supports")
    name = models.CharField(verbose_name=_("Name"), max_length=255, default="", blank=True)
    relate = models.CharField(verbose_name=_("Relate"), max_length=255, default="", blank=True)
    nationality = models.CharField(verbose_name=_("nationality"), default="", max_length=255, blank=True)
    date_of_birth=models.DateField(verbose_name=_("Date of Birth"), blank=True, null=True)
    national_number = models.CharField(verbose_name=_("National Number"), default="", blank=True, max_length=255)
    notes = models.CharField(verbose_name=_("Notes"), default="", blank=True, max_length=255)

class Brother(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="brothers")
    name = models.CharField(default="", max_length=255, blank=True)
    relate = models.CharField(verbose_name=_("Relate"), max_length=255, default="", blank=True)
    qualification = models.CharField(verbose_name=_("Qualification"), max_length=255, blank=True, default="")
    job = models.CharField(verbose_name=_("Job"), max_length=255, default="", blank=True)
    military_officer = models.BooleanField(default=False)
    spouse_name = models.CharField(verbose_name=_("Spouse Name"), max_length=255, default="", blank=True)
    spouse_qualification = models.CharField(verbose_name=_("Qualification"), max_length=255, blank=True, default="")
    spouse_job = models.CharField(verbose_name=_("Job"), max_length=255, blank=True, default="")
    residence = models.CharField(verbose_name=_("Residence"), max_length=255, default="", blank=True)

    def __str__(self):
        return f"{self.name}"

class RelativeQuerySet(models.QuerySet):
    def father_relates(self):
        return self.filter(relate='عم')
    
    def mother_relates(self):
        return self.filter(relate='خال')

class RelativeManager(models.Manager):
    pass

class Relative(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="relatives")
    relate = models.CharField(default="", choices=[
        ('عم', _('عم')),
        ('خال', _('خال')),
    ], max_length=255, blank=True)
    name = models.CharField(default="", max_length=255, blank=True)
    qualification = models.CharField(verbose_name=_("Qualification"), max_length=255, blank=True, default="")
    job = models.CharField(verbose_name=_("Job"), max_length=255, default="", blank=True)
    spouse_name = models.CharField(verbose_name=_("Spouse Name"), default="", max_length=255, blank=True)
    spouse_job = models.CharField(verbose_name=_("Spouse Job"), default="", max_length=255, blank=True)
    residence = models.CharField(verbose_name=_("Residence"), max_length=255, default="", blank=True)

    objects=RelativeManager.from_queryset(queryset_class=RelativeQuerySet)()

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
            return age
        return None  
    
    def __str__(self):
        return f"{self.name}"
    

class Current_Wife_QuerySet(models.QuerySet):
    def male_count(self):
        return self.filter(gender='male').count()
    
    def female_count(self):
        return self.filter(gender='female').count()

class Current_Wife_Data(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="current_wife_data")
    statement = models.CharField(verbose_name=_("Statement"), max_length=255, choices=[
        ('الزوجة', _("الزوجة")),
        ('والدها', _('والدها')),
        ('والدتها', _("والدتها")),
    ])
    name = models.CharField(verbose_name=_("Name"), max_length=255, default="", blank=True)
    nationality = models.CharField(max_length=255, blank=True, default="مصري")
    religion = models.CharField(verbose_name=_("Religion"), default="مسلم", max_length=255)
    qualification = models.CharField(verbose_name=_("Qualification"), max_length=255, default="", blank=True)
    job = models.CharField(verbose_name=_("Job"), max_length=255, blank=True, default="")
    residence = models.CharField(verbose_name=_("Residence"), max_length=255, blank=True, default="")

class Wife_Manager(models.Manager):
    pass

class Wife_Borther(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="wife_brothers")
    name = models.CharField(verbose_name=_("Name"), max_length=255, default="", blank=True)
    gender = models.CharField(verbose_name=_("Gender"), max_length=255, choices=[
        ('male', _("Male")),
        ('female', _("Female")),
    ])
    qualification = models.CharField(verbose_name=_("Qualification"), max_length=255, default="", blank=True)
    job = models.CharField(verbose_name=_("Job"), max_length=255, blank=True, default="")
    spouse_name = models.CharField(verbose_name=_("Spouse Name"), default="", max_length=255, blank=True)
    spouse_job = models.CharField(verbose_name=_("Spouse Job"), default="", max_length=255, blank=True)
    residence = models.CharField(verbose_name=_("Residence"), max_length=255, default="", blank=True)

    objects = Wife_Manager.from_queryset(queryset_class=Current_Wife_QuerySet)()




