# Generated by Django 4.2 on 2023-05-27 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_product_color_product_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name_cat',
        ),
    ]
