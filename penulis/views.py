from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import (CreateUserForm,)
# Create your views here.

def register(requets):
    form = CreateUserForm()
    if requets.method == 'POST':
        form = CreateUserForm(requets.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(
                '<script>alert("register atas username'+username+'");window.location="'+reverse_lazy('penulis:login')+'";</script>'
            )
    context = {
        'form':form,
        'page_title':'Register Page',
    }
    return render(requets,'penulis/register.html',context)

def loginView(requets):
    if requets.method == 'POST':
        username = requets.POST.get('username')
        password = requets.POST.get('password')
        
        user = authenticate(requets, username=username, password = password)
        
        if user is not None:
            login(requets,user)
            return redirect('artikel:home')
        else:
            return HttpResponse('<script>alert("username or password is incorrect, try again");window.location="'+reverse_lazy('penulis:login')+'";</script>')
    context = {
        'page_title':'Login Page',
    }
    return render(requets,'penulis/login.html',context)
