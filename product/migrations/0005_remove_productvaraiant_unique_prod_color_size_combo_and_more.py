# Generated by Django 4.2 on 2023-05-21 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_brand_colour_productvaraiant_size_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='productvaraiant',
            name='unique_prod_color_size_combo',
        ),
        migrations.RemoveField(
            model_name='productvaraiant',
            name='amount_in_stock',
        ),
    ]
