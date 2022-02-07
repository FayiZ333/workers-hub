# Generated by Django 4.0.1 on 2022-02-07 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=333)),
                ('address', models.TextField(max_length=333)),
                ('phone', models.BigIntegerField()),
                ('district', models.CharField(max_length=333)),
                ('city', models.CharField(max_length=333)),
                ('time_from', models.DateTimeField()),
                ('time_to', models.DateTimeField()),
                ('requierments', models.TextField(max_length=333)),
                ('budget', models.IntegerField()),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
