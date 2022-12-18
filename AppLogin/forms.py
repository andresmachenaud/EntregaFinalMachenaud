from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from ckeditor_uploader.fields import RichTextUploadingField

class AvatarForm(forms.Form):
    imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class UserEditForm(UserCreationForm): #no es un UserCreationForm porque permite cambios en el Perfil y no solo en User
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name","last_name","email", "password1", "password2"]
        help_texts = { "email": "Indica un correo electronico que uses habitualmente", "first_name": "", "last_name": "", "password1": ""}

class PerfilEditForm(ModelForm):
    descripcion = models.TextField(max_length=500, null=True,blank=True)
    link = models.CharField(null=True,max_length=100,blank=True)

    class Meta:
        model = Perfil
        fields = ["descripcion","link"]
        help_texts = { "descripcion": "Escribe una breve descripción sobre ti", "link": "Indica un link a tus redes sociales"}

    