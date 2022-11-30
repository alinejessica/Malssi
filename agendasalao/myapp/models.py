from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=10)
    meta = models.IntegerField()

class Funcionario(models.Model) :
    cpf = models.CharField (max_length=11)
    procedimento = models.ForeignKey(max_length=20)
    ativo = models.BooleanField(max_length= 1) 
    gerente = models.BooleanField

class Agendamento (models.Model):
    data_agendamento = models.IntegerField()
    horário_agendamento = models.IntegerField()
    funcionario = models.ForeignKey(Funcionario)
