from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key= True)
    nome = models.TextField(max_length = 255)
    

class Checkbox(models.Model):
    titulo = models.TextField(max_length = 200)
    tarefa = models.BooleanField(default= False)
    def __str__(self):
        return self.titulo
