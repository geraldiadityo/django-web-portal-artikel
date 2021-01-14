from django import forms
from django.forms import Select,Textarea
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
            'penulis':Select,
            'isi':Textarea
        }
    def __init__(self, *args, **kwargs):
        super(AritikeForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widgets.attrs.update({
                'class':'form-control',
            })

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

