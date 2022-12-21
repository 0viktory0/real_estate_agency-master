# Generated by Django 2.2.24 on 2022-12-19 11:04

from django.db import migrations


def load_flats(apps, schema_editor):
    Flat = apps.get_model('property','Flat')
    Owner = apps.get_model('property','Owner')
    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(name=flat.owner, pure_phone=flat.pure_phone)
        owner_flat = owner[0].flats
        owner_flat.set([flat])

def load_flat_owners(apps, schema_editor):
    Flat = apps.get_model('property','Flat')
    Owner = apps.get_model('property','Owner')
    for owner in Owner.objects.all():
        flat = Flat.objects.get_or_create(owner=owner.name, pure_phone=owner.pure_phone)
        flat_owner = flat[0].owner
        flat_owner.set([owner])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20221218_2328'),
    ]

    operations = [
        migrations.RunPython(load_flats, load_flat_owners, ),
    ]
