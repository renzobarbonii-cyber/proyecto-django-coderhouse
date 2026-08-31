from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(
        max_length=100
    )

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    biografia = models.TextField(
        blank=True
    )

    telefono = models.CharField(
        max_length=30,
        blank=True
    )

    ciudad = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"Perfil de {self.usuario.username}"


class Publicacion(models.Model):
    titulo = models.CharField(
        max_length=200
    )

    contenido = models.TextField()

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo