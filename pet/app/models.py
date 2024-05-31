from django.db import models
from django.contrib.auth.models import AbstractUser
from .extensions import CITIES

class User(AbstractUser):
    """ Extended Django built-in User model"""

    otc = models.CharField(max_length=30, null=True, blank=True)
    tg_name = models.CharField(max_length=15, blank=False)
    is_sitter = models.BooleanField(default=False, blank=False)
    city = models.CharField(choices=CITIES, default='EVN', max_length=3)
    address = models.CharField(max_length=150, null=True)


class Sitter(models.Model):
    pass


class Owner(models.Model):
    pass


class Admin(models.Model):
    pass


class Keep(models.Model):
    pass


class Feedback(models.Model):
    pass
