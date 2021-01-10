from django.urls import path

from .views import *
app_name = 'artikel'

urlpatterns = [
    path('',ArtikelListView.as_view(),name='home'),
]