# Generated by Django 2.2.24 on 2022-12-17 16:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='flats', to=settings.AUTH_USER_MODEL, verbose_name='Лайк'),
        ),
    ]