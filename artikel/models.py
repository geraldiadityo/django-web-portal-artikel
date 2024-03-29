from django.db import models
from django.utils.text import slugify
# Create your models here
from penulis.models import *
class Artikel(models.Model):
    judul = models.CharField(max_length=200,null=True)
    isi = models.TextField(null=True)
    KATEGORI_TYPE = (
        ('JURNAL','Jurnal'),
        ('GOSIP','Gosip'),
        ('TRAVELING','Traveling'),
    )
    kategori = models.CharField(null=True, blank=True, choices=KATEGORI_TYPE,max_length=200)
    penulis = models.ForeignKey(Penulis,null=True,on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, editable=False)
    published = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()
    
    def __str__(self):
        return "{}".format(self.judul)

