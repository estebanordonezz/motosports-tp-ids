from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Moto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="motos", null=True, blank=True, default=None)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.categoria} - {self.marca} {self.modelo} ({self.año})"