# Generated by Django 3.2 on 2021-04-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_rename_sing_category_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='sign',
            field=models.CharField(default='exclamation', max_length=30),
        ),
    ]
