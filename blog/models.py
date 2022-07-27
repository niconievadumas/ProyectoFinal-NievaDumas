from urllib import request
from django.db import models
from ckeditor.fields import RichTextField


class Posteo(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    contenido = RichTextField(null=True)
    autor = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(null=True)    
    imagen = models.ImageField(upload_to='posteos', blank=True)
 
    def __str__(self):
        return f"{self.titulo} - Autor : {self.autor}"     


       