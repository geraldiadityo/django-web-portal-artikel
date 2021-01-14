from django.urls import path
from .views import *
app_name = 'penulis'

urlpatterns = [
    path('login/',loginView,name='login'),
    path('register/',register,name='register'),
]