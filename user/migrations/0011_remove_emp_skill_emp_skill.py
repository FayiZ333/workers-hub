# Generated by Django 4.0.1 on 2022-02-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_emp_skill1_emp_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='skill',
        ),
        migrations.AddField(
            model_name='emp',
            name='skill',
            field=models.ManyToManyField(to='user.Skill'),
        ),
    ]
