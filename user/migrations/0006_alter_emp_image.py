# Generated by Django 4.0.1 on 2022-02-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_emp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='image',
            field=models.ImageField(upload_to='emp'),
        ),
    ]