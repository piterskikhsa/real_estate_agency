# Generated by Django 2.2.4 on 2019-08-15 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20190815_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_deprecated',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_pure',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
