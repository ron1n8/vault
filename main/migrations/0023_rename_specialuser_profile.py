# Generated by Django 3.2 on 2021-04-14 08:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('main', '0022_specialuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpecialUser',
            new_name='Profile',
        ),
    ]