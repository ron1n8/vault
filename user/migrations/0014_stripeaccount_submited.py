# Generated by Django 3.2 on 2021-05-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_author_paypal_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripeaccount',
            name='submited',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
