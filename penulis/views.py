from django.shortcuts import render,redirect
from django.views.generic import DetailView
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import (CreateUserForm,AritikeForm, PenulisForm)
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

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def artikelList(request):
    artikels = request.user.penulis.artikel_set.all().order_by('-published')
    context = {
        'artikel':artikels,
    }
    return render(request,'penulis/manage_artikel.html',context)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def artikel_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            artikels = request.user.penulis.artikel_set.all().order_by('-published')
            data['html_artikel_list'] = render_to_string('penulis/manage_artikel_list.html',{'artikel':artikels})
        else:
            data['form_is_valid'] = False
    context = {
        'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def createArtikel(request):
    penulis = request.user.penulis
    if request.method == 'POST':
        form = AritikeForm(request.POST)
    else:
        form = AritikeForm(initial={'penulis':penulis})
    return artikel_save_form(request,form,'penulis/partartikelcreate.html')

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def updateArtikel(request,pk):
    artikel = request.user.penulis.artikel_set.get(id=pk)
    if request.method == 'POST':
        form = AritikeForm(request.POST,instance=artikel)
    else:
        form = AritikeForm(instance=artikel)
    return artikel_save_form(request,form,'penulis/partartikelupdate.html')

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def deleteArtikel(request,pk):
    artikel = request.user.penulis.artikel_set.get(id=pk)
    data = dict()
    if request.method == 'POST':
        artikel.delete()
        data['form_is_valid'] = True
        artikels = request.user.penulis.artikel_set.all().order_by('-published')
        data['html_artikel_list'] = render_to_string('penulis/manage_artikel_list.html',{'artikel':artikels},request=request)
    else:
        context = {
            'artikel':artikel,
        }
        data['html_form'] = render_to_string('penulis/partartikeldelete.html',context,request=request)
    return JsonResponse(data)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def detailArtikel(request,slug):
    artikel = request.user.penulis.artikel_set.get(slug=slug)
    context = {
        'page_title':'Detail Artikel',
        'artikel':artikel,
    }
    return render(request,'penulis/detail_artikel.html',context)

@login_required(login_url='penulis:login')
@allowed_user(allowed_roles=['penulis'])
def profileSetting(request):
    penulis = request.user.penulis
    form = PenulisForm(instance=penulis)
    if request.method == 'POST':
        form = PenulisForm(request.POST, request.FILES, instance=penulis)
        if form.is_valid():
            form.save()
            return HttpResponse(
                '<script>alert("profile success updated");window.location="'+str(reverse_lazy('penulis:profile_setting'))+'";</script>'
            )
    context = {
        'form':form,
        'page_title':'Profile Setting',
    }
    return render(request,'penulis/profile_setting.html',context)
