# Generated by Django 3.2 on 2021-05-02 09:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_alter_author_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bday',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 9, 3, 55, 314827, tzinfo=utc)),
        ),
    ]
