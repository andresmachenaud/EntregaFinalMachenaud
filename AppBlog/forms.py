from django import forms 
from django.forms import ModelForm
from .models import *

class EntradaFormulario(ModelForm):

    class Meta:
        model = Entrada
        fields = (
            'titulo',
            'subtitulo',
            'libro',
            'calificacion',
            'cuerpo',
            'imagen',
        )

# class LibroFormulario(forms.Form): #no es un UserCreationForm porque permite cambios en el Perfil y no solo en User
#     categorias = [("Arte", "Arte"), ("Biografía","Biografía"), ("Negocios","Negocios"), ("Infantil","Infantil"), ("Comics","Comics"), ("Cocina","Cocina"), ("Fantasía","Fantasía"), ("Ficción","Ficción"), ("Novela gráfica","Novela gráfica"),
#             ("Ficción histórica","Ficción histórica"), ("Histora","Histora"), ("Terror","Terror"), ("Música","Música"), ("Misterio","Misterio"), ("Poesía","Poesía"), ("Piscología","Piscología"), ("Romántico","Romántico"), ("Ciencia","Ciencia"),
#             ("Ciencia Ficción","Ciencia Ficción"), ("Autoayuda","Autoayuda"), ("Deportes","Deportes"), ("Suspenso","Suspenso"), ("Turismo","Turismo"), ("Juvenil","Juvenil") ]

#     titulo = forms.CharField(max_length=100)
#     autor = forms.CharField(max_length=100)
#     ano = forms.IntegerField(validators=[MaxValueValidator(datetime.date.today().year)])
#     categoria = forms.ChoiceField(choices=categorias)
#     editorial = forms.CharField(max_length=100)

class LibroFormulario(ModelForm):

     class Meta:
         model = Libro
         fields = (
             'titulo',
             'autor',
             'ano',
             'categoria',
             'editorial',
         )

class ComentarioFormulario(ModelForm):

    class Meta:
        model = Comentario
        fields = (
            'cuerpo',
        )

class MensajeFormulario(ModelForm):

    class Meta:
        model = Mensaje
        fields = (
            'cuerpo',
        )

class EditarEntradaFormulario(ModelForm):
    imagen = forms.ImageField(required = False)
    
    class Meta:
        model = Entrada
        fields = (
            'titulo',
            'subtitulo',
            'calificacion',
            'cuerpo',
            'imagen',
        )
        