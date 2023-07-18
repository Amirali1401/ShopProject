# Generated by Django 4.2 on 2023-05-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_order_zarinpal_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zarinpal_ref_id',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AlterField(
            model_name='order',
            name='zarinpal_authority',
            field=models.CharField(max_length=255),
        ),
    ]