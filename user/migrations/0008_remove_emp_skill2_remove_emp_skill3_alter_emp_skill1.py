# Generated by Django 4.0.1 on 2022-02-02 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='skill2',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='skill3',
        ),
        migrations.AlterField(
            model_name='emp',
            name='skill1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.skill'),
        ),
    ]