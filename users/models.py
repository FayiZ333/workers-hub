from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class myaccount(BaseUserManager):
    def create_user(self, email, username, phone, password=None, profile_img=None):
        if not email:
            raise ValueError("Users must have an email id")
        if not username:
            raise ValueError("Users must have an username")
        if not phone:
            raise ValueError("Users must have an phone No")

        user  = self.model(
                email=self.normalize_email(email),
                username=username,
                phone=phone,
                profile_img=profile_img,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user  = self.model(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class Custom(AbstractBaseUser):
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name          = models.CharField(max_length=33, unique=True)
    last_name           = models.CharField(max_length=33, unique=True)
    phone               = models.IntegerField(max_length=15)
    address             = models.TextField(max_length=333,null=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = myaccount()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email 

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True
