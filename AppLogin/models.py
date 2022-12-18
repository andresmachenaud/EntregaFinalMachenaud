from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=500, null=True,blank=True)
    link = models.CharField(null=True,max_length=100,blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
