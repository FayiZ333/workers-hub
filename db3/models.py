from django.db import models

# Create your models here.


class Emp2(models.Model):
    name = models.CharField(max_length=33)
    address = models.CharField(max_length=33)
    email = models.EmailField(max_length=33)

    def __str__(self):
        return self.name