from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.template import context

def home_view(request):
    return render(request, 'mainApp/basic.html')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'register/register.html', context={'form': form})
    return render(request, 'mainApp/basic.html', context={'form': form})
    return render(request, 'mainApp/include/main.html', context={'form': form})