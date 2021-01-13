from django.urls import path,re_path

from .views import *
app_name = 'artikel'

urlpatterns = [
    re_path(r'^artikel/(?P<page>\d+)/$',ArtikelListView.as_view(),name='home'),
    re_path(r'^artikel/detail/(?P<slug>[\w-]+)/$',ArtikelDetailView,name='detail'),
    re_path(r'^artikel/kategori/(?P<kategori>[\w]+)/(?P<page>\d+)/$',ArtikelKategoriListView,name="kategori-list"),
]