# Generated by Django 3.2 on 2021-05-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_delete_bank'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=10)),
                ('currency', models.CharField(max_length=10)),
                ('business_link', models.URLField()),
                ('charges_enabled', models.BooleanField()),
                ('transfers', models.BooleanField()),
                ('external_account', models.JSONField()),
            ],
        ),
        migrations.RenameField(
            model_name='author',
            old_name='bank_account',
            new_name='stripe_account',
        ),
    ]