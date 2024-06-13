# Generated by Django 3.2.25 on 2024-06-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='Default Country', max_length=40),
        ),
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, default='Default County', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default='Default Street Address', max_length=80),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='town_city',
            field=models.CharField(default='Default Town', max_length=40),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]