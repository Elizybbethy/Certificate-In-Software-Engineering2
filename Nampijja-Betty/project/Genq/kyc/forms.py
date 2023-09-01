from .models import *
from django import forms
from django.forms import ModelForm

class RegisterForm(forms.ModelForm):
    dateofbirth =forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model= Register
        fields ='__all__'
        # fields =[
        #     'hee',
        # ]