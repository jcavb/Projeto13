from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, default='', null=True) 
    senha = models.CharField(max_length=255, default='')

    def save(self, *args, **kwargs):
        self.senha = make_password(self.senha)
        super(Usuario, self).save(*args, **kwargs)

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
