from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
# Create your views here.

from .models import Artikel

class ArtikelPerkategori():
    model = Artikel
    
    def get_last_artikel_each_kategori(self):
        kategoriList = self.model.objects.values_list('kategori',flat=True).distinct()
        queryset = []
        for kategori in kategoriList:
            artikel = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(artikel)
        return queryset

class BlogHomeView(TemplateView,ArtikelPerkategori):
    template_name = 'artikel/home_view.html'

    def get_context_data(self):
        data = self.get_last_artikel_each_kategori()
        context = {
            'page_title':'Wellcome',
            'dataKategori':data,
        }
        return context

class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_list.html'
    context_object_name = 'artikel'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        kategoriList = self.model.objects.values_list('kategori',flat=True).distinct()
        data_context = {
            'page_title':'Artikel',
            'kategorilist':kategoriList,
        }
        self.kwargs.update(data_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_kategori_list.html'
    context_object_name = 'artikel'
    ordering = ['-published']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori = self.kwargs['kategori'])
        return super().get_queryset()
    
    def get_context_data(self,*args, **kwargs):
        kategoriList = self.model.objects.values_list('kategori',flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        data_context = {
            'page_title':self.kwargs['kategori'],
            'kategorilist':kategoriList,
        }
        self.kwargs.update(data_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel/artikel_detail.html'
    context_object_name = 'artikel'

    def get_context_data(self, *args, **kwargs):
        artikelSerupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id = self.object.id)
        data_context = {
            'page_title':'Detail Artikel',
            'artikelSerupa':artikelSerupa,
        }
        self.kwargs.update(data_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
