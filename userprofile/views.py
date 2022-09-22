from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# def dashboard(request):
#     form = ProfileForm
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance = request.user)
#         # user = request.user
        
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Saved successfully")
#             # phone = form.cleaned_data['phone']
#             # address = form.cleaned_data['address']
#             # user = Profile.objects.filter(user = user).update(phone=phone, address=address)
#             return redirect('/store')
#         else:
#             print(form)
#             messages.info(request, 'Invalid credentials')
#             return redirect('dashboard')
#     return render(request, 'dashboard.html',{"form": form})
def register(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signed Up successfully')
            return redirect('/login')
        else:
            print(form)
            messages.info(request, 'Invalid credentials')
            return redirect('register_user')
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # print(f"user" + " is logged in" )
            print(user, "is logged in")
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            print(username, password)
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        print( user, "is logged out" )
    else:
        print("no user is currently logged in")
    return redirect("login")


@login_required
def dashboard(request):
    if request.method =='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your details have been updated')
            return redirect('dashboard')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    load_up = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', load_up)