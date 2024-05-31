from django.db import models
from django.contrib.auth.models import AbstractUser
from .extensions import CITIES, ANIMALS, SPECIES, GENDER

class User(AbstractUser):
    """ Extended Django built-in User model"""

    otc = models.CharField(max_length=30, null=True, blank=True)
    tg_name = models.CharField(max_length=15, blank=False)
    is_sitter = models.BooleanField(default=False, blank=False)
    city = models.CharField(choices=CITIES, default='EVN', max_length=3)
    address = models.CharField(max_length=150, null=True)


class Sitter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True)
    social = models.URLField(null=True)
    about = models.TextField(null=True)
    animals = models.CharField(choices=ANIMALS, default='NO', max_length=3)
    passport = models.IntegerField(null=True)
    ppt_img = models.ImageField(upload_to='passports/', null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    rating = models.FloatField(default=0.0)
    game = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)


class Pet(models.Model):
    species = models.CharField(choices=SPECIES, default='CAT', max_length=3)
    breed = models.CharField(null=True, max_length=150)
    name = models.CharField(max_length=15, null=True)
    gender = models.CharField(choices=GENDER, default='MAL', max_length=3)
    sterilized = models.BooleanField(default=True)
    birth_year = models.DateField(null=True)
    weigth = models.FloatField(default=0.0)
    immunized = models.BooleanField(default=True)
    vet_ppt = models.BooleanField(default=True)
    emergency_contact = models.CharField(max_length=250, null=True)
    disease = models.BooleanField(default=False)
    features = models.TextField(max_length=700, null=True)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(default=0.0)
    notes = models.TextField(max_length=500, null=True)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    employee_id = models.CharField(max_length=255, null=True)


class Keep(models.Model):
    pass


class Feedback(models.Model):
    pass
