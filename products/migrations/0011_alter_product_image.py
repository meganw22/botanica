# Generated by Django 3.2.25 on 2024-06-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_plantprice_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(
                default='media/no-image-available.png', upload_to='media/'),
        ),
    ]
