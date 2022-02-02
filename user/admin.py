from django.contrib import admin
from .models import Emp, User

# Register your models here.

admin.site.register(User)
admin.site.register(Emp)