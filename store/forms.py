from django import forms
from django.forms import ModelForm
from .models import Registration



class ClientForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        
        widgets = {
            'first_name':forms.TextInput(attrs={'type':'text', 'id':'FNAME', 'placeholder':'First name',}),
            'last_name':forms.TextInput(attrs={'type':'text', 'id':'LNAME', 'placeholder':'Last name',}),
            'phone':forms.TextInput(attrs={'type':'tel', 'id':'Phone', 'placeholder': 'Primary phone number'}),
            'email': forms.TextInput(attrs={'type':'email', 'id':'Email', 'placeholder': 'Email address'}),
            'password1': forms.TextInput(attrs={'type':'password', 'id':'Password', 'placeholder':'password'}),
            'password2': forms.TextInput(attrs={'type':'password', 'id':'Password', 'placeholder':'password'})
            }