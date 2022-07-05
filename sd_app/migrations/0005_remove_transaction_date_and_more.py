# Generated by Django 4.0.5 on 2022-07-05 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0004_transaction_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user_profile',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='delivery_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
