from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from .extensions import *


class User(AbstractUser):
    """ Extended Django built-in User model"""

    email = models.EmailField(blank=False, max_length=254, unique=True, verbose_name='Почта')
    patronym = models.CharField(max_length=30, null=True, blank=True, verbose_name='Отчество')
    tg_name = models.CharField(max_length=15, blank=False, verbose_name='Телеграм ник')
    city = models.CharField(choices=CITIES, default='EVN', max_length=3, verbose_name='Город')
    address = models.CharField(max_length=150, null=True, verbose_name='Адрес')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        # "username"
    ]

    def __str__(self):
        return f"Пользователь {self.id} {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Sitter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='ID пользователя')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения')
    social = models.URLField(null=True, verbose_name='Ссылка на соц. сеть')
    about = models.TextField(null=True, verbose_name='О себе')
    home = models.CharField(null=True, choices=HOME, max_length=4, verbose_name='Тип жилья')
    animals = models.CharField(choices=ANIMALS, default='NO', max_length=3, verbose_name='Животные дома')
    avatar = models.ImageField(upload_to='avatars/', null=True, verbose_name='Фото профиля')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')
    game = models.BooleanField(default=False, verbose_name='Прохождение игры')
    activated = models.BooleanField(default=False, verbose_name='Аккаунт активирован')

    def __str__(self):
        return f"Ситтер {self.id} {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Ситтер"
        verbose_name_plural = "Ситтеры"


class HomeImages(models.Model):
    image = models.ImageField(upload_to='home/', null=True, verbose_name='Фото дома')
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE, verbose_name='ID ситтера', related_name='images')

    def __str__(self):
        return f"Ситтер {self.sitter.user.id} {self.sitter.user.first_name} {self.sitter.user.last_name}"

    class Meta:
        verbose_name = "Фото дома"
        verbose_name_plural = "Фото дома"


class Passport(models.Model):
    """ Model representing sitters' passport data. Permission must be limited """

    # TODO надо выяснить как выглядит армянский паспорт
    sitter = models.OneToOneField(Sitter, on_delete=models.CASCADE, verbose_name='ID ситтера', null=True)
    pass_num = models.IntegerField(null=True,
                                   validators=[MaxValueValidator(9999999999)],
                                   verbose_name='Серия и номер паспорта')
    given_dt = models.DateField(null=True, verbose_name='Дата выдачи')
    given_code = models.IntegerField(null=True,
                                     validators=[MaxValueValidator(999999)],
                                     verbose_name='Код подразделения')
    given_nm = models.TextField(max_length=500, null=True, verbose_name='Наименование подразделения')
    first_nm = models.CharField(max_length=255, null=True, verbose_name='Имя владельца')
    second_nm = models.CharField(max_length=255, null=True, verbose_name='Фамилия владельца')
    sur_nm = models.CharField(max_length=255, null=True, blank=True, verbose_name='Отчество владельца')
    birth_dt = models.DateField(null=True, verbose_name='Дата рождения')
    addr_nm = models.TextField(max_length=500, null=True, verbose_name='Адрес прописки')
    pic_1 = models.ImageField(upload_to=f'passports/sitter', null=True, verbose_name='Фото паспорта')
    pic_2 = models.ImageField(upload_to=f'passports/sitter', null=True, verbose_name='Фото паспорта')

    def __str__(self):
        return f"Паспорт - {self.second_nm} {self.first_nm[:1:]}. {self.sur_nm[:1:]}."

    class Meta:
        verbose_name = "Паспортные данные"
        verbose_name_plural = "Паспортные данные"


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='ID пользоваетеля')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')
    notes = models.TextField(max_length=500, null=True, verbose_name='Заметки администратора')

    def __str__(self):
        return f"Владелец {self.id} {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"


class Pet(models.Model):
    species = models.CharField(choices=SPECIES, null=True, max_length=3, verbose_name='Вид животного')
    breed = models.CharField(null=True, max_length=150, verbose_name='Порода')
    name = models.CharField(max_length=15, null=True, verbose_name='Кличка')
    gender = models.CharField(choices=GENDER, null=True, max_length=3, verbose_name='Пол')
    sterilized = models.BooleanField(default=False, verbose_name='Кастрация')
    birth_year = models.DateField(null=True, verbose_name='Год рождения')
    weigth = models.FloatField(default=0.0, verbose_name='Вес')
    immunized = models.BooleanField(default=False, verbose_name='Вакцинация')
    vet_ppt = models.BooleanField(default=False, verbose_name='Ветеринарный паспорт')
    emergency_contact = models.CharField(max_length=250, null=True, verbose_name='Контакт для экстренных случаев')
    diseases = models.CharField(default='Нет', max_length=255, verbose_name='Патологии')
    fears = models.CharField(max_length=255, null=True, verbose_name='Страхи')
    features = models.TextField(max_length=700, null=True, verbose_name='Особенности')
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, null=True, verbose_name='ID владельца')

    # Для котиков
    outside_lb = models.CharField(choices=OUTSIDE_LB, null=True, blank=False, max_length=3, verbose_name='Ходит мимо лотка?')
    scratch = models.CharField(null=True, blank=False, max_length=255, verbose_name='Дерет мебель?')

    # Для собак
    pulls = models.CharField(choices=PULLS, null=True, blank=False, max_length=3, verbose_name='Тянет поводок?')
    picks = models.CharField(choices=PICKS, null=True, blank=False, max_length=3, verbose_name='Подбирает с земли?')
    take = models.CharField(choices=TAKE, null=True, blank=False, max_length=3, verbose_name='Можно отобрать?')
    aggression = models.CharField(choices=AGGRESSION, null=True, blank=False, max_length=3, verbose_name='Агрессии?')
    no_leash = models.CharField(choices=NO_LEASH, null=True, blank=False, max_length=3, verbose_name='Можно без поводка?')
    dogs_contact = models.CharField(choices=DOGS_CONTACT, null=True, blank=False, max_length=3, verbose_name='Контакт с др. собаками?')
    wash_paws = models.CharField(choices=WASH_PAWS, null=True, blank=False, max_length=4, verbose_name='Как моют лапы?')
    pee_home = models.CharField(choices=PEE_HOME, null=True, blank=False, max_length=3, verbose_name='Туалет дома?')
    gnaw_home = models.CharField(choices=GNAW_HOME, null=True, blank=False, max_length=3, verbose_name='Грызет вещи?')
    walk = models.CharField(choices=WALK, null=True, blank=False, max_length=2, verbose_name='Сколько гулять?')


    def __str__(self):
        return f"{self.id} {self.species.lower()} {self.name} {self.owner.user.last_name}"

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='ID пользователя')
    employee_id = models.CharField(max_length=255, null=True, verbose_name='Номер сотрудника')

    def __str__(self):
        return f"Администратор {self.employee_id} {self.user.last_name}"

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Keep(models.Model):
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, null=True, verbose_name='Заказчик/Владелец')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, verbose_name='Питомец')
    sitter = models.OneToOneField(Sitter, on_delete=models.CASCADE, null=True, verbose_name='Ситтер')
    from_date = models.DateField(verbose_name='Начало передержки', null=True)
    to_date = models.DateField(verbose_name='Конец передержки', null=True)
    other_pets = models.CharField(choices=OTHER_PETS, null=True, blank=False, max_length=3,
                                  verbose_name='Может жить с другими животными?')
    feed = models.CharField(choices=FEED, null=True, blank=False, max_length=1,
                            verbose_name='Сколько р/день кормить?')
    pick_up = models.CharField(choices=PICK_UP, null=True, blank=False, max_length=2,
                               verbose_name='Заберете до 12 или после?')
    transfer = models.CharField(choices=TRANSFER, null=True, blank=False, max_length=2,
                                verbose_name='Как передадите питомца?')

    def __str__(self):
        return f"Передержка {self.id} {self.owner.user.last_name} {self.sitter.user.last_name}"

    class Meta:
        verbose_name = "Передержка"
        verbose_name_plural = "Передержки"


class SitterFeedback(models.Model):
    sitter = models.OneToOneField(Sitter, on_delete=models.CASCADE, verbose_name='Ситтер')
    author = models.OneToOneField(Owner, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(max_length=500, verbose_name='Отзыв', null=True)
    image = models.ImageField(upload_to='sitter-feedback/', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return f"Ситтер {self.sitter.user.email}"

    class Meta:
        verbose_name = "Отзыв о ситтере"
        verbose_name_plural = "Отзывы о ситтерах"


class Feedback(models.Model):

    def __str__(self):
        return f"Отзыв {self.id}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
