import email
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=40, null=False)
    password = models.CharField(max_length=50, null=False)
    
class Customer(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=False)
    products = models.CharField(max_length=50, null=False)
    
class Product(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)
    price = models.IntegerField(max_length=10, null=False)
    image = models.ImageField(upload_to='media')