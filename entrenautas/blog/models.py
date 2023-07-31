from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    # Puedes añadir más campos aquí según lo necesites

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    # Puedes añadir más campos aquí según lo necesites
