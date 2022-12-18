from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
from AppLogin.models import *
from django.utils import timezone

# Create your models here.

class Libro(models.Model):

    categorias = [("Arte", "Arte"), ("Biografía","Biografía"), ("Negocios","Negocios"), ("Infantil","Infantil"), ("Comics","Comics"), ("Cocina","Cocina"), ("Fantasía","Fantasía"), ("Ficción","Ficción"), ("Novela gráfica","Novela gráfica"),
            ("Ficción histórica","Ficción histórica"), ("Histora","Histora"), ("Terror","Terror"), ("Música","Música"), ("Misterio","Misterio"), ("Poesía","Poesía"), ("Piscología","Piscología"), ("Romántico","Romántico"), ("Ciencia","Ciencia"),
            ("Ciencia Ficción","Ciencia Ficción"), ("Autoayuda","Autoayuda"), ("Deportes","Deportes"), ("Suspenso","Suspenso"), ("Turismo","Turismo"), ("Juvenil","Juvenil") ]

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField(validators=[MaxValueValidator(datetime.date.today().year)])
    categoria = models.CharField(max_length=100, choices=categorias)
    editorial = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=False, blank=False)
    fecha = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now=True, null=True, blank=True)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE, null=False, blank = False)
    calificacion = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    cuerpo = RichTextUploadingField()
    imagen = models.ImageField()

    def __str__(self):
        return f"{self.titulo}"

    def numcomentarios(self):
        cant=Comentario.objects.filter(post_id=self.id).count()
        return cant

class Comentario(models.Model):
    post = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=False, blank=False)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cuerpo

    def get_avatar(self):
        avatar=Avatar.objects.filter(user_id=self.autor.user_id)
        if avatar:
            return avatar[0].imagen.url
        else:
            return None        

class Mensaje(models.Model):
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=False, blank=False)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.cuerpo} "

    def get_avatar(self):
        avatar=Avatar.objects.filter(user_id=self.autor.user_id)
        if avatar:
            return avatar[0].imagen.url
        else:
            return None
