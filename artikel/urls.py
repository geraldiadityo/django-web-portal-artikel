from django.urls import path,re_path

from .views import *
app_name = 'artikel'

urlpatterns = [
    re_path(r'^artikel/(?P<page>\d+)/$',ArtikelListView.as_view(),name='home'),
]