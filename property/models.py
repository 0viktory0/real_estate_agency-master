from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

BUILDING_TYPES = ((True, 'Да'), (False, 'Нет'), (None, "Неизвестно"))

class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField(
        'Новостройка:',
        choices=BUILDING_TYPES,
        blank=True,
        null=True)
    likes = models.ManyToManyField(
        User,
        related_name='flats',
        blank=True,
        verbose_name='Лайк')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Кто жаловался:',
        null=True,
        on_delete=models.SET_NULL)
    flat = models.ForeignKey(
        Flat,
        verbose_name='Квартира, на которую пожаловались:',
        null=True,
        on_delete=models.SET_NULL)
    text = models.TextField(
        verbose_name='Текст жалобы:',
        null=True)


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20, db_index=True)
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True, db_index=True)

    owner_flats = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        related_name='owners')

    def __str__(self):
        return f'{self.name}, {self.owner_pure_phone}'