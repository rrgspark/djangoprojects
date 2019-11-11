from django.db import models

class Item(models.Model):
    descripcion = models.CharField(max_length=255)
    completado = models.BooleanField(default=False)
