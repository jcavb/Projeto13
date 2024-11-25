from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import timedelta

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, default='', null=True) 
    senha = models.CharField(max_length=255, default='')

    def save(self, *args, **kwargs):
        self.senha = make_password(self.senha)
        super(Usuario, self).save(*args, **kwargs)


class Tarefa(models.Model):
    CATEGORIA_CHOICES = [
        ('REGA', 'Rega'),
        ('COLHEITA', 'Colheita'),
    ]

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.nome


class Cultura(models.Model):
    nome = models.CharField(max_length=100)
    temperatura_ideal = models.CharField(max_length=50)
    tipo_solo = models.CharField(max_length=100)
    rotacao_cultivo = models.CharField(max_length=100)
    umidade_ideal = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class ChecklistItem(models.Model):
    nome = models.CharField(max_length=100)
    marcado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Lembrete(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    atividade = models.CharField(max_length=255)
    data_lembrete = models.DateTimeField()  # Alterado para DateTimeField
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.atividade

