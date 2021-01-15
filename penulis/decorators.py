from django.http import HttpResponse
from django.shortcuts import render, redirect

def unauthenticated_user(view_func):
    def wrapper_func(requets, *args, **kwargs):
        if requets.user.is_authenticated:
            return redirect('penulis:home')
        else:
            return view_func(requets, *args, **kwargs)
    return wrapper_func

def allowed_user(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<script>alert("You are not authorized in this page");</script>')
        return wrapper_func
    return decorator

