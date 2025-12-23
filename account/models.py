from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique= True)
    owner_name = models.CharField(max_length=100, null=False)
    email  =models.EmailField(max_length=254, unique= True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#class MenuItem  

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    decription = models.TextField(blank = True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

#CLASS CUSTOmusermanager 
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError('Email needed!')
        email = self.normalize_email(email)
        #creates user instance based on custom user model
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('restaurant', None)
        return self.create_user(email, password, **extra_fields)
    

# customuser model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank= False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE , null=True, blank= True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

# class Customer

class Customer(models.Model):
    name= models.CharField(default="Guest", max_length=100)
    phone= models.CharField(blank=True, null=True, max_length=15)
    email= models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or 'Guest Customer'