# Generated by Django 3.2.25 on 2024-06-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='TEMP_STRIPE_PID', max_length=254),
            preserve_default=False,
        ),
    ]
