from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,fullname,password=None,**extra_fields):
        if not fullname:
            raise ValueError("fullname must be provided")
        user = self.model(fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, fullname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(fullname, password, **extra_fields)