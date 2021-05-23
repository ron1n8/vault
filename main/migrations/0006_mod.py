# Generated by Django 2.2.19 on 2021-04-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0005_delete_mod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=40)),
                ('model_author', models.CharField(max_length=20)),
                ('model_desc', models.TextField()),
                ('model_prise', models.CharField(max_length=20)),
                ('model_date', models.DateTimeField()),
                ('model_image', models.ImageField(upload_to='')),
                ('model_file', models.FileField(upload_to='storage/')),
                ('model_views', models.IntegerField()),
                ('model_downloads', models.IntegerField()),
            ],
        ),
    ]
