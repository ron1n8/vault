# Generated by Django 3.2 on 2021-05-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_paymentsession_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
