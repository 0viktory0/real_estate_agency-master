# Generated by Django 2.2.24 on 2022-12-18 20:26

from django.db import migrations
import phonenumbers


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for building in Flat.objects.all().iterator():
        building.owner_pure_phone = phonenumbers.parse(building.owners_phonenumber, 'RU')
        building.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for building in Flat.objects.all():
        building.owner_pure_phone = None
        building.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20221217_2200'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone, move_backward)
    ]
