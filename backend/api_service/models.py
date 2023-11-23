from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("You must provide an email!")
        if not first_name:
            raise ValueError("You must provide your last name!")
        if not last_name:
            raise ValueError("You must provide your last name!")
        
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )
        user.set_password(password)
        user.save(using='default')
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using='default')
        return user
    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=40, unique=True, null=True)
    api_key_created_at = models.DateTimeField(auto_now_add=True)
    api_key_last_used_at = models.DateTimeField(null=True, blank=True)
    api_key_status = models.CharField(max_length=20, default='active', choices=[('active', 'Active'), ('inactive', 'Inactive')])
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

