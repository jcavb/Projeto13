from django.db import models # type: ignore
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


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
    data_ultima_acao = models.DateField()
    concluida = models.BooleanField(default=False)

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
    
class Tarefa(models.Model):
    descricao = models.CharField(max_length=255)
    dia = models.DateField()
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
    

class Atividade(models.Model):
    TIPO_ATIVIDADE_CHOICES = [
        ('producao', 'Produção'),
        ('colheita', 'Colheita'),
        ('cuidados', 'Cuidados'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_ATIVIDADE_CHOICES)
    descricao = models.TextField()
    data_realizacao = models.DateField()
    realizada = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.descricao[:20]} ({self.data_realizacao})"
