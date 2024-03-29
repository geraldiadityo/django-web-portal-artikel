from django.urls import path,re_path

from .views import *
app_name = 'artikel'

urlpatterns = [
    re_path(r'^profile-penulis/(?P<pk>\d+)/$',get_profile_penulis,name='profile_penulis'),
    re_path(r'^artikel/(?P<page>\d+)/$',ArtikelListView.as_view(),name='home'),
    re_path(r'^artikel/detail/(?P<slug>[\w-]+)/$',ArtikelDetailView.as_view(),name='detail'),
    re_path(r'^artikel/kategori/(?P<kategori>[\w]+)/(?P<page>\d+)/$',ArtikelKategoriListView.as_view(),name="kategori-list"),
    path('',BlogHomeView.as_view(),name='index_home'),
]