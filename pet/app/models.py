from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from .extensions import CITIES, ANIMALS, SPECIES, GENDER


class User(AbstractUser):
    """ Extended Django built-in User model"""

    email = models.EmailField(blank=False, max_length=254, unique=True)
    patronym = models.CharField(max_length=30, null=True, blank=True)
    tg_name = models.CharField(max_length=15, blank=False)
    is_sitter = models.BooleanField(default=False, blank=False)
    city = models.CharField(choices=CITIES, default='EVN', max_length=3)
    address = models.CharField(max_length=150, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        # "username"
    ]


class Passport(models.Model):
    """ Model representing sitters' passport data. Permission must be limited """

    # TODO надо выяснить как выглядит армянский паспорт
    pass_num = models.IntegerField(null=True, validators=[MaxValueValidator(9999999999)]) # номер паспорта, с серией
    given_dt = models.DateField(null=True) # дата выдачи
    birth_dt = models.DateField(null=True) # дата рождения
    given_code = models.IntegerField(validators=[MaxValueValidator(999999)], null=True) # код подразделения выдачи паспорта
    given_nm = models.TextField(max_length=500, null=True) # наименование подразделения выдачи
    first_nm = models.CharField(max_length=255, null=True) # Имя владельца
    second_nm = models.CharField(max_length=255, null=True) # Фамилия владельца
    sur_nm = models.CharField(max_length=255, null=True, blank=True) # Отчество владельца
    addr_nm = models.TextField(max_length=500, null=True) # Адрес по прописке
    pic_img = models.ImageField(upload_to='passports/', null=True) # Фото паспорта


class Sitter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True)
    social = models.URLField(null=True)
    about = models.TextField(null=True)
    animals = models.CharField(choices=ANIMALS, default='NO', max_length=3)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    rating = models.FloatField(default=0.0)
    game = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE, null=True)


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
