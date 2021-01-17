from django.urls import path,re_path
from .views import *
app_name = 'penulis'

urlpatterns = [
    re_path(r'^update/(?P<pk>\d+)/$',updateArtikel,name='update_artikel'),
    re_path(r'^delete/(?P<pk>\d+)/$',deleteArtikel,name='delete_artikel'),
    re_path(r'detail-artikel/(?P<slug>[\w-]+)/$',detailArtikel,name='detail_artikel'),
    path('create/',createArtikel,name='create_artikel'),
    path('manage/',artikelList,name='manage'),
    path('login/',loginView,name='login'),
    path('register/',register,name='register'),
    path('logout/',logoutView,name='logout'),
    path('',home,name='home'),
]