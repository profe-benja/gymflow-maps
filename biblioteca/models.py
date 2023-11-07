from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Maquina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    img = models.ImageField(upload_to='maquinas/', null=True, blank=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)
    maquinas = models.ManyToManyField(Maquina)
    def __str__(self):
        return self.user.username + ' - ' + self.role

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    estado = models.IntegerField(default=1)


