from django.shortcuts import render, redirect
from .models import *
from.forms import *

# Create your views here.
def base(request):
    return render(request, 'base.html')

# This is for the base
def form(request):
    # return render(request, 'base.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = RegisterForm()
    return render(request, 'form.html', {'form': form})

def success(request):
    context = {
        'message': "Thank you for registering!",
        
    };
    return render(request, 'success.html', context)

    