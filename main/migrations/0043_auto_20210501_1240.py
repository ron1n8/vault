# Generated by Django 3.2 on 2021-05-01 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_remove_mod_model_downloads'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notifications',
            field=models.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='author',
            name='bday',
            field=models.DateTimeField(default=datetime.date(2021, 5, 1)),
        ),
    ]
