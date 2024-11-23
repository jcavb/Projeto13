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
    
class Culturas(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Rotacoes(models.Model):
    nome = models.CharField(max_length=100)
    cultura = models.ForeignKey(Culturas, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.nome
