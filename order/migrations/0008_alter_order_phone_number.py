# Generated by Django 4.2 on 2023-05-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
