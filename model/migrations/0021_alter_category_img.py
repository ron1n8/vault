# Generated by Django 4.0 on 2022-04-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0020_alter_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to='static/storage/img/categories'),
        ),
    ]
