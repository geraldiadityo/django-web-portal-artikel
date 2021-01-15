from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import (CreateUserForm,)
from .decorators import unauthenticated_user,allowed_user
from artikel.models import Artikel
# Create your views here.

@unauthenticated_user
def register(requets):
    form = CreateUserForm()
    if requets.method == 'POST':
        form = CreateUserForm(requets.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(
                '<script>alert("register atas username'+str(username)+'");window.location="'+str(reverse_lazy('penulis:login'))+'";</script>'
            )
    context = {
        'form':form,
        'page_title':'Register Page',
    }
    return render(requets,'penulis/register.html',context)

@unauthenticated_user
def loginView(requets):
    if requets.method == 'POST':
        username = requets.POST.get('username')
        password = requets.POST.get('password')
        
        user = authenticate(requets, username=username, password = password)
        
        if user is not None:
            login(requets,user)
            return redirect('penulis:home')
        else:
            return HttpResponse('<script>alert("username or password is incorrect, try again");window.location="'+str(reverse_lazy('penulis:login'))+'";</script>')
    context = {
        'page_title':'Login Page',
    }
    return render(requets,'penulis/login.html',context)

@login_required(login_url='penulis:login')
def logoutView(request):
    logout(request)
    return redirect('penulis:login')

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def home(request):
    artikel = request.user.penulis.artikel_set.all().order_by('-published')
    kategorilist = request.user.penulis.artikel_set.values_list('kategori',flat=True).distinct()
    context = {
        'page_title':'Home Artikel',
        'artikel':artikel,
        'kategorilist':kategorilist,
    }
    return render(request,'penulis/penulis_artikel_home.html',context)

