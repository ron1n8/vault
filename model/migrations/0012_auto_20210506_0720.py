# Generated by Django 3.2 on 2021-05-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0011_alter_mod_model_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='model_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='mod',
            name='model_price',
            field=models.IntegerField(),
        ),
    ]
