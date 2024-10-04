from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key= True)
    nome = models.TextField(max_length = 255)
    

class Checkbox(models.Model):
    titulo = models.TextField(max_length = 200)
    tarefa = models.BooleanField(default= False)
    def __str__(self):
        return self.titulo

from django.db import models

class Tarefa(models.Model):
    CATEGORIA_CHOICES = [
        ('REGA', 'Rega'),
        ('COLHEITA', 'Colheita'),
    ]

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    data_ultima_acao = models.DateField()
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
