from django import forms
from django.forms import Select,Textarea,TextInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from artikel.models import Artikel

class AritikeForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = [
            'judul',
            'kategori',
            'penulis',
            'isi',
        ]
        widgets = {
            'judul':TextInput,
            'kategori':TextInput,
            'penulis':Select(
                attrs={
                    'disabled':'true',
                }
            ),
            'isi':Textarea
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'email':'Your Email',
        }
        

