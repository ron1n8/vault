# Generated by Django 3.2 on 2021-05-04 09:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bday',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 9, 43, 58, 304650, tzinfo=utc)),
        ),
    ]
