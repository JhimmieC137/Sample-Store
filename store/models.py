import email
from django.db import models
from userprofile.models import Profile
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    # phone = PhoneNumberField()
    email = models.EmailField(max_length=40, null=False)
    username = models.CharField(max_length=40, null=False)
    password = models.CharField(max_length=50, null=False)
    
class Customer(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=False)
    products = models.CharField(max_length=50, null=False)
    
class Product(models.Model):
    name = models.CharField(max_length=20, null=False) 
    description = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='products')
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    products = models.  ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    date_of_transaction = models.DateTimeField(max_length=200, null=True)