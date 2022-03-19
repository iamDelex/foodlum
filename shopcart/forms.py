from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from shopcart.models import *


class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart
        fields = ['quantity','how_spicey']