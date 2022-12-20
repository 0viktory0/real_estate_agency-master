# Generated by Django 2.2.24 on 2022-12-17 16:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, verbose_name='Нормализованный номер владельца'),
        ),
    ]
