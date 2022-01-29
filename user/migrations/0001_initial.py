# Generated by Django 4.0.1 on 2022-01-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=333, unique=True)),
                ('last_name', models.CharField(max_length=333, unique=True)),
                ('email', models.CharField(max_length=333, unique=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(max_length=333, null=True)),
                ('password', models.CharField(max_length=333)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]