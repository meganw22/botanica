# Generated by Django 3.2.25 on 2024-06-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20240621_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(max_length=254),
        ),
    ]