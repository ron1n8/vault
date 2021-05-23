# Generated by Django 3.2 on 2021-05-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20210510_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='reports',
            field=models.JSONField(default=[]),
        ),
        migrations.AddField(
            model_name='author',
            name='warnings',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
