# Generated by Django 4.2 on 2023-05-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_authority',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
