# Generated by Django 4.0 on 2022-03-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0017_auto_20210524_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to='E:\\Server\\Projects\\aviatorsstatic/storage/img/categories'),
        ),
    ]
