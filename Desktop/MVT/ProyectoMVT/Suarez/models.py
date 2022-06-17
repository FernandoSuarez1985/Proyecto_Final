from django.db import models


class Familia(models.Model):
    name = models.CharField(max_length=40)
    edad = models.FloatField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    vivo = models.BooleanField(default=True)

