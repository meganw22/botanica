# Generated by Django 3.2.25 on 2024-06-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_stripe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
