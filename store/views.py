from django.shortcuts import render
from .forms import ClientForm
from .models import Product, Customer
# Create your views here.


def home(request):
    return render(request, 'home.html') 

def register(request):
    if request.method == 'POST':
        pass
    else:
        form = ClientForm
        return render(request, "register.html", {'form': form})