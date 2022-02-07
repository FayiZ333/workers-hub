from unicodedata import category
from django.db import models
from user.models import User

# Create your models here.

class Form(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    category            = models.CharField(max_length=333)
    address             = models.TextField(max_length=333)
    phone               = models.BigIntegerField()
    district            = models.CharField(max_length=333)
    city                = models.CharField(max_length=333)
    time_from           = models.DateField()
    time_to             = models.DateField()
    requierments        = models.TextField(max_length=333)
    budget              = models.IntegerField()
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active           = models.BooleanField(default=True)

    def __str__(self):
        return self.user

    