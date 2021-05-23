# Generated by Django 3.2 on 2021-04-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0016_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=40)),
                ('model_author', models.CharField(max_length=20)),
                ('model_desc', models.TextField()),
                ('model_prise', models.CharField(max_length=20)),
                ('model_date', models.DateTimeField()),
                ('model_image', models.ImageField(upload_to='static/storage/img/models')),
                ('model_file', models.FileField(upload_to='static/storage/models')),
                ('model_views', models.IntegerField(default=0)),
                ('model_downloads', models.IntegerField(default=0)),
            ],
        ),
    ]