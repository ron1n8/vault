# Generated by Django 3.2 on 2021-04-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210420_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sing',
            field=models.CharField(default='star-half', max_length=30),
        ),
    ]
