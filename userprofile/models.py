from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    phone = PhoneNumberField(null=True)
    address = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    