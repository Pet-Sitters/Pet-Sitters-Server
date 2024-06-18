from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from .extensions import CITIES, ANIMALS, HOME, SPECIES, GENDER, PULLS, PICKS, TAKE, AGGRESSION, NO_LEASH, \
    DOGS_CONTACT, WASH_PAWS, PEE_HOME, GNAW_HOME, WALK, OUTSIDE_LB, OTHER_PETS, FEED, \
    PICK_UP, TRANSFER, STATUS


class CustomUser(AbstractUser):
    """ Extended Django built-in User model"""

    username = models.EmailField(blank=False, max_length=254, unique=True, verbose_name='Почта')

    def __str__(self):
        return f"{self.id}. Пользователь {self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Sitter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, verbose_name='ID пользователя', blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    patronym = models.CharField(max_length=30, null=True, blank=True, verbose_name='Отчество')
    tg_nick = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телеграм ник')
    tg_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телеграм ID')
    phone_num = models.CharField(max_length=15, null=True, blank=True, verbose_name='Номер телефона')
    city = models.CharField(choices=CITIES, default='EVN', max_length=3, verbose_name='Город', blank=True)
    address = models.CharField(max_length=150, null=True, verbose_name='Адрес', blank=True)
    birth_date = models.DateField(null=True, verbose_name='Дата рождения', blank=True)
    social = models.URLField(null=True, verbose_name='Ссылка на соц. сеть', blank=True)
    about = models.TextField(null=True, verbose_name='О себе', blank=True)
    home = models.CharField(null=True, choices=HOME, max_length=4, verbose_name='Тип жилья', blank=True)
    animals = models.CharField(choices=ANIMALS, default='NO', max_length=3, verbose_name='Животные дома', blank=True)
    # avatar = models.ImageField(upload_to='avatars/', null=True, verbose_name='Фото профиля', blank=True)
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг', blank=True)
    game = models.BooleanField(default=False, verbose_name='Прохождение игры', blank=True)
    activated = models.BooleanField(default=False, verbose_name='Аккаунт активирован', blank=True)

    def __str__(self):
        return f"{self.id}. Ситтер {self.last_name} {self.first_name[:1:]}. {self.patronym[:1:]}."

    class Meta:
        verbose_name = "Ситтер"
        verbose_name_plural = "Ситтеры"


class HomeImages(models.Model):
    image = models.ImageField(upload_to='home/', null=True, verbose_name='Фото дома', blank=True)
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE, verbose_name='ID ситтера', related_name='images', blank=True)

    def __str__(self):
        return f"Ситтер {self.sitter.id}"

    class Meta:
        verbose_name = "Фото дома"
        verbose_name_plural = "Фото дома"


class Passport(models.Model):
    """ Model representing sitters' passport data. Permission must be limited """

    # TODO надо выяснить как выглядит армянский паспорт
    sitter = models.OneToOneField(Sitter, on_delete=models.CASCADE, verbose_name='ID ситтера', null=True, blank=True)
    pass_num = models.IntegerField(null=True,
                                   validators=[MaxValueValidator(9999999999)],
                                   verbose_name='Серия и номер паспорта', blank=True)
    given_dt = models.DateField(null=True, verbose_name='Дата выдачи', blank=True)
    given_code = models.IntegerField(null=True,
                                     validators=[MaxValueValidator(999999)],
                                     verbose_name='Код подразделения', blank=True)
    given_nm = models.TextField(max_length=500, null=True, verbose_name='Наименование подразделения', blank=True)
    first_nm = models.CharField(max_length=255, null=True, verbose_name='Имя владельца', blank=True)
    second_nm = models.CharField(max_length=255, null=True, verbose_name='Фамилия владельца', blank=True)
    sur_nm = models.CharField(max_length=255, null=True, blank=True, verbose_name='Отчество владельца')
    birth_dt = models.DateField(null=True, verbose_name='Дата рождения', blank=True)
    addr_nm = models.TextField(max_length=500, null=True, verbose_name='Адрес прописки', blank=True)
    # pic_1 = models.ImageField(upload_to=f'passports/sitter', null=True, verbose_name='Фото паспорта', blank=True)
    # pic_2 = models.ImageField(upload_to=f'passports/sitter', null=True, verbose_name='Фото паспорта', blank=True)

    def __str__(self):
        return f"Паспорт {self.second_nm} {self.first_nm[:1:]}. {self.sur_nm[:1:]}."

    class Meta:
        verbose_name = "Паспортные данные"
        verbose_name_plural = "Паспортные данные"


class Owner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='ID пользоваетеля')
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    patronym = models.CharField(max_length=30, null=True, blank=True, verbose_name='Отчество')
    tg_nick = models.CharField(max_length=15, blank=True, verbose_name='Телеграм ник')
    tg_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телеграм ID')
    phone_num = models.CharField(max_length=15, null=True, blank=True, verbose_name='Номер телефона')
    city = models.CharField(choices=CITIES, default='EVN', max_length=3, verbose_name='Город', blank=True)
    address = models.CharField(max_length=150, null=True, verbose_name='Адрес', blank=True)
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг', blank=True)
    notes = models.TextField(max_length=500, null=True, verbose_name='Заметки администратора', blank=True)

    def __str__(self):
        # return f"{self.id}. Владелец {self.last_name} {self.first_name[:1:]}. {self.patronym[:1:]}."
        return f"Владелец {self.id}"

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"


class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='Владелец', blank=True)
    species = models.CharField(choices=SPECIES, null=True, max_length=3, verbose_name='Вид животного', blank=True)
    breed = models.CharField(null=True, max_length=150, verbose_name='Порода', blank=True)
    name = models.CharField(max_length=15, null=True, verbose_name='Кличка', blank=True)
    gender = models.CharField(choices=GENDER, null=True, max_length=3, verbose_name='Пол', blank=True)
    sterilized = models.BooleanField(default=False, verbose_name='Кастрация', blank=True)
    birth_year = models.DateField(null=True, verbose_name='Год рождения', blank=True)
    weigth = models.FloatField(default=0.0, verbose_name='Вес', blank=True)
    immunized = models.BooleanField(default=False, verbose_name='Вакцинация', blank=True)
    vet_ppt = models.BooleanField(default=False, verbose_name='Ветеринарный паспорт', blank=True)
    emergency_contact = models.CharField(max_length=250, null=True, blank=True,
                                         verbose_name='Контакт для экстренных случаев')
    diseases = models.CharField(default='Нет', max_length=255, verbose_name='Патологии', blank=True)
    fears = models.CharField(max_length=255, null=True, verbose_name='Страхи', blank=True)
    features = models.TextField(max_length=700, null=True, verbose_name='Особенности', blank=True)

    # Для котиков
    outside_lb = models.CharField(choices=OUTSIDE_LB, null=True, blank=True, max_length=3,
                                  verbose_name='Ходит мимо лотка?')
    scratch = models.CharField(null=True, blank=True, max_length=255, verbose_name='Дерет мебель?')

    # Для собак
    pulls = models.CharField(choices=PULLS, null=True, blank=True, max_length=3, verbose_name='Тянет поводок?')
    picks = models.CharField(choices=PICKS, null=True, blank=True, max_length=3, verbose_name='Подбирает с земли?')
    take = models.CharField(choices=TAKE, null=True, blank=True, max_length=3, verbose_name='Можно отобрать?')
    # aggression = models.CharField(choices=AGGRESSION, null=True, blank=True, max_length=255, verbose_name='Агрессии?')
    aggression = models.CharField(null=True, blank=True, max_length=255, verbose_name='Агрессии?')
    no_leash = models.CharField(choices=NO_LEASH, null=True, blank=True, max_length=3,
                                verbose_name='Можно без поводка?')
    dogs_contact = models.CharField(choices=DOGS_CONTACT, null=True, blank=True, max_length=3,
                                    verbose_name='Контакт с др. собаками?')
    wash_paws = models.CharField(choices=WASH_PAWS, null=True, blank=True, max_length=4, verbose_name='Как моют лапы?')
    pee_home = models.CharField(choices=PEE_HOME, null=True, blank=True, max_length=3, verbose_name='Туалет дома?')
    gnaw_home = models.CharField(choices=GNAW_HOME, null=True, blank=True, max_length=3, verbose_name='Грызет вещи?')
    walk = models.CharField(choices=WALK, null=True, blank=True, max_length=2, verbose_name='Сколько гулять?')

    def __str__(self):
        return f"{self.id}. {self.name}"

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, verbose_name='ID пользователя', blank=True)
    employee_id = models.CharField(max_length=255, null=True, verbose_name='Номер сотрудника', blank=True)

    def __str__(self):
        return f"Администратор {self.employee_id} {self.last_name}"

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Keep(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Заказчик/Владелец')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Питомец')
    sitter = models.OneToOneField(Sitter, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ситтер')
    from_date = models.DateField(verbose_name='Начало передержки', null=True, blank=True)
    to_date = models.DateField(verbose_name='Конец передержки', null=True, blank=True)
    other_pets = models.CharField(choices=OTHER_PETS, null=True, blank=True, max_length=3,
                                  verbose_name='Может жить с другими животными?')
    feed = models.CharField(choices=FEED, null=True, blank=True, max_length=1,
                            verbose_name='Сколько р/день кормить?')
    pick_up = models.CharField(choices=PICK_UP, null=True, blank=True, max_length=2,
                               verbose_name='Заберете до 12 или после?')
    transfer = models.CharField(choices=TRANSFER, null=True, blank=True, max_length=2,
                                verbose_name='Как передадите питомца?')
    status = models.CharField(choices=STATUS, max_length=10, verbose_name='Заказ активен',
                              null=True, blank=True)

    def __str__(self):
        # return f"{self.id}. Передержка: {self.owner.last_name} {self.pet.name} {self.sitter.last_name}"
        return f"{self.id}. Передержка: {self.owner.last_name}"

    class Meta:
        verbose_name = "Передержка"
        verbose_name_plural = "Передержки"


class ShortForm(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True)
    keep = models.ForeignKey(Keep, on_delete=models.CASCADE, verbose_name='Новая передержка', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Имя', blank=True)
    tg_nick = models.CharField(max_length=255, verbose_name='Телеграм', blank=True)
    phone_num = models.IntegerField(validators=[MaxValueValidator(99999999999)], verbose_name='Номер телефона', blank=True)

    def __str__(self):
        return f"{self.id}. Короткая форма {self.name} - {self.tg_nick}"

    class Meta:
        verbose_name = "Короткая форма"
        verbose_name_plural = "Короткие формы"


class SitterFeedback(models.Model):
    sitter = models.OneToOneField(Sitter, on_delete=models.CASCADE, verbose_name='Ситтер', blank=True)
    author = models.OneToOneField(Owner, on_delete=models.CASCADE, verbose_name='Автор', blank=True)
    content = models.TextField(max_length=500, verbose_name='Отзыв', null=True, blank=True)
    image = models.ImageField(upload_to='sitter-feedback/', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return f"{self.id}. Отзыв о {self.sitter.last_name} от {self.author.last_name}"

    class Meta:
        verbose_name = "Отзыв о ситтере"
        verbose_name_plural = "Отзывы о ситтерах"


class Feedback(models.Model):

    def __str__(self):
        return f"{self.id}. Отзыв "

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
