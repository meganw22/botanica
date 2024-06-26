# Generated by Django 3.2.25 on 2024-05-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('easy_name', models.CharField(max_length=200)),
                ('scientific_name', models.CharField(
                    blank=True, max_length=200, null=True)),
                ('height', models.CharField(max_length=200)),
                ('care_level', models.CharField(max_length=200)),
                ('light_level', models.CharField(max_length=200)),
                ('price', models.DecimalField(
                    decimal_places=2, max_digits=5)),
                ('image', models.ImageField(
                    blank=True, null=True, upload_to='')),
            ],
        ),
    ]
