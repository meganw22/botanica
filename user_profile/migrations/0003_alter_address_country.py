# Generated by Django 3.2.25 on 2024-06-27 21:26

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20240621_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(blank=True, null=True),
        ),
    ]
