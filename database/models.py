from datetime import date

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from user.models import Recruit

class Parent(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="parents")
    relate = models.CharField(default="", choices=[
        ('الوالد', _('الوالد')),
        ('الوالده', _('الوالده')),
        ('الجد', _('الجد')),
        ('الجده', _('الجده')),
    ], max_length=255, blank=True)
    name = models.CharField(default="", max_length=255, blank=True)
    religion = models.CharField(default="", max_length=255, blank=True)
    nationality = models.CharField(default="", max_length=255, blank=True)
    job = models.TextField(null=True, blank=True)
    date_of_birth=models.DateField(null=True, blank=True)
    birth_location = models.CharField(default="", max_length=255, blank=True) 
    residence = models.TextField(null=True, blank=True)  

    def __str__(self):
        return f"{self.name}"

class Brother(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name="brothers")
    name = models.CharField(default="", max_length=255, blank=True)
    date_of_birth=models.DateField(null=True, blank=True)
    job = models.TextField(null=True, blank=True)
    wife_name = models.CharField(default="", max_length=255, blank=True)
    wife_job = models.CharField(default="", max_length=255, blank=True)
    residence = models.TextField(null=True, blank=True)

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
    date_of_birth = models.DateField(null=True, blank=True)
    job = models.TextField(null=True, blank=True)
    wife_name = models.CharField(default="", max_length=255, blank=True)
    wife_job = models.CharField(default="", max_length=255, blank=True)
    residence = models.TextField(null=True, blank=True)

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
