# Generated by Django 3.2 on 2021-05-10 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_stripeaccount_submited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stripeaccount',
            old_name='submited',
            new_name='submitted',
        ),
    ]