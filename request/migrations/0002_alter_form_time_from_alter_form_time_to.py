# Generated by Django 4.0.1 on 2022-02-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='time_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='time_to',
            field=models.DateField(),
        ),
    ]
