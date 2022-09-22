from email import message
from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib import messages
import datetime



# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def create_order(request, id):
    product = Product.objects.get(id=id)
    order = Order(customer = request.user.profile, products=product, date_of_transaction=datetime.datetime.now())
    order.save()
    return redirect('home')