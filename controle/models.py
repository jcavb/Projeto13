from django.db import models

class Fertilizante(models.Model):
    fertilizante = models.CharField(max_length=100)
    imagem = models.URLField(max_length=300)

class Semente(models.Model):
    semente = models.CharField(max_length=100)
    imagem = models.URLField(max_length=300)