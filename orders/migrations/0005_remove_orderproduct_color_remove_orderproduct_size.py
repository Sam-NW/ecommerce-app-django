# Generated by Django 4.2 on 2023-05-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
    ]
