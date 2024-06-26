# Generated by Django 3.2.25 on 2024-06-11 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_plantprice_size'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses'},
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='products.product'
                ),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item_total',
            field=models.DecimalField(
                decimal_places=2,
                editable=False,
                max_digits=10,
                null=True),
        ),
    ]
