# Generated by Django 3.2 on 2021-05-02 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_author_vipstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='credit',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='bday',
            field=models.DateTimeField(default=datetime.date(2021, 5, 2)),
        ),
    ]
