from django.db import models # type: ignore

class Fertilizante(models.Model):
    fertilizante = models.CharField(max_length=100)
    imagem = models.URLField(max_length=300)

    def __str__(self):
        return self.fertilizante

class Semente(models.Model):
    semente = models.CharField(max_length=100)
    imagem = models.URLField(max_length=300)

    def __str__(self):
        return self.semente