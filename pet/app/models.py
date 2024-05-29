from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ Extended Django built-in User model"""

    tg_name = models.CharField(max_length=15, blank=False)
    is_sitter = models.BooleanField(default=False, blank=False)


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
