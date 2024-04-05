from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import RecuritManager

# Create your models here.
class Recruit(AbstractBaseUser, PermissionsMixin):
    code = models.CharField(max_length=50, unique=True, db_index=True, null=False)

    name = models.CharField(default="", max_length=255, blank=True)
    education = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    birth_location = models.CharField(default="", max_length=255, blank=True)
    marital_status = models.CharField(default="", max_length=255, blank=True)
    number_of_children = models.PositiveIntegerField(default=0)
    residence = models.TextField(null=True, blank=True)
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
