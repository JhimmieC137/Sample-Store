from django.contrib import admin
from .models import Registration, Customer, Product
# Register your models here.

admin.site.register(Registration)
admin.site.register(Customer)
admin.site.register(Product)