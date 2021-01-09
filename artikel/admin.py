from django.contrib import admin
from .models import Artikel
# Register your models here.
class AritkelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'updated',
        'published',
    ]

admin.site.register(Artikel,AritkelAdmin)