# Generated by Django 4.2 on 2023-05-06 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='agent_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
