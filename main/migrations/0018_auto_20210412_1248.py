# Generated by Django 3.2 on 2021-04-12 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_category_mod'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Mod',
        ),
    ]
