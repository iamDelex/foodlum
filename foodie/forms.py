from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from foodie.models import *



class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Username')
    first_name = forms.CharField(max_length=30, help_text='First name')
    last_name = forms.CharField(max_length=30, help_text='Last name')
    email = forms.EmailField(max_length=30, help_text='Email')
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','phone','subject', 'message']
        
STATE = [
    ('Abia', 'Abia'),
    ('Abuja', 'Abuja'),
    ('Edo', 'Edo'),
    ('Kano', 'Kano'),
    ('Lagos', 'Lagos'),
    ('Ogun', 'Ogun'),
    ('PH', 'PH'),
]



       
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'address', 'state', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}),
            'state': forms.Select(attrs={'class':'form-control', 'placeholder':'state'}, choices=STATE),
            'image': forms.FileInput(attrs={'class':'form-control', 'placeholder':'image'})
        }
        
        
