# Generated by Django 3.2 on 2021-05-11 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0015_mod_model_author_price'),
        ('payment', '0007_debt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt',
            name='modelset',
        ),
        migrations.AddField(
            model_name='debt',
            name='model',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='model.mod'),
            preserve_default=False,
        ),
    ]
