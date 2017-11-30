from django import forms
from .models import Posts, Comment
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields=[
            "Nombre",
            "Edad",
            "Raza",
            "Estado",
            "Informacion",
            "Descripcion",
            "Foto",



        ]

class users_form(UserCreationForm):
    name=forms.CharField(max_length=50)
    Edad=forms.IntegerField()
    Telefono=forms.IntegerField()
    Email=forms.CharField(max_length=50)
    Direccion=forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    Descripcion=forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    Foto=forms.ImageField()

class CommentForm(forms.Form):
    content_type=forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))



