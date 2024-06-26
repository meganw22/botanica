# Generated by Django 3.2.25 on 2024-06-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantprice',
            name='size',
            field=models.CharField(choices=[
                ('sm', 'Small'),
                ('md', 'Medium'),
                ('lg', 'Large')
                ], max_length=10),
        ),
        migrations.AlterField(
            model_name='plantsize',
            name='size',
            field=models.CharField(choices=[
                ('sm', 'Small'),
                ('md', 'Medium'),
                ('lg', 'Large')],
                max_length=10),
        ),
    ]
