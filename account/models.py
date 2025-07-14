# account/models.py
from django.db import models

from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class CustomUser(AbstractBaseUser,PermissionsMixin):
    ROLE_CHOICE = (
        ('user','User'),
        ('vendor','Vendor'),
        ('superadmin','SuperAdmin')
    )

    fullname = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=10,unique=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICE,default='user')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'fullname'
    REQUIRED_FIELDS = ['phone', 'role']

    def __str__(self):
        return f"{self.fullname} ({self.role})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users' 