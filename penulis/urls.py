from django.urls import path,re_path
from .views import *
app_name = 'penulis'

urlpatterns = [
    re_path(r'^update/(?P<pk>\d+)/$',updateArtikel,name='update_artikel'),
    path('create/',createArtikel,name='create_artikel'),
    path('login/',loginView,name='login'),
    path('register/',register,name='register'),
    path('logout/',logoutView,name='logout'),
    path('',home,name='home'),
]