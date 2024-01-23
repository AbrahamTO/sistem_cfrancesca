from django.db import models

class zapatos(models.Model):
    codigo=models.AutoField(primary_key=True)
    color=models.CharField(max_length=50)
    talla=models.PositiveSmallIntegerField()
    modelo=models.CharField(max_length=100)
    taco=models.PositiveSmallIntegerField(null=True,blank=True)
    caracteristicas=models.TextField(blank=True)
    categoria=models.CharField(max_length=100)
    precio=models.PositiveIntegerField()
    fecha_vendida=models.DateTimeField(null=True, blank=True)
    vendido = models.BooleanField(default=False, blank=True)