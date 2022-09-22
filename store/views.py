from email import message
from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Product, Customer, Registration, Order
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
import datetime



# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def create_order(request, id):
    product = Product.objects.get(id=id)
    order = Order(customer = request.user.profile, products=product, date_of_transaction=datetime.datetime.now())
    order.save()
    print(order.date_of_transaction)
    return redirect('home')