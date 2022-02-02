from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class myaccount(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email id")
        if not first_name:
            raise ValueError("Users must have an first_name")
        if not last_name:
            raise ValueError("Users must have an last_name")
        user  = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user  = self.model(
                email=self.normalize_email(email),
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    first_name          = models.CharField(max_length=333)
    last_name           = models.CharField(max_length=333)
    email               = models.CharField(max_length=333, unique=True)
    phone               = models.BigIntegerField(null=True, blank=True)
    address             = models.TextField(max_length=333,null=True)
    password            = models.CharField(max_length=333)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = myaccount()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


class Emp(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    image               = models.ImageField(upload_to='emp')
    skill1              = models.CharField(max_length=333)
    skill2              = models.CharField(max_length=333, null=True, blank=True)
    skill3              = models.CharField(max_length=333, null=True, blank=True)
    city                = models.CharField(max_length=333)
    description         = models.TextField(max_length=333, null=True, blank=True)
    subscription        = models.CharField(max_length=333)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_worker           = models.BooleanField(default=False)


    def __str__(self):
        return self.email
