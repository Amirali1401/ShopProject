# Generated by Django 4.2 on 2023-05-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]