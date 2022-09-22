from email import message
from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Product, Customer, Registration
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def home(request):
    return render(request, 'home.html')