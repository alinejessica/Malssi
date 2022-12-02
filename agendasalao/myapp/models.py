from django.db import models

class Funcionario(models.Model) :
    cpf = models.CharField (max_length=11)
    procedimento = models.ForeignKey(max_length=20)
    ativo = models.BooleanField(max_length= 1) 
    gerente = models.BooleanField



class Cadastro (models.Model):
    nome = models.CharField(max_length=10)
    sobrenome = models.CharField(max_length=50) 
    email = models.CharField(max_length=30) 
    senha = models.CharField(max_length=10) 
    telefone =  models.IntegerField(11) 
    data_de_nasc = models.IntegerField()
    endereco = models.CharField(max_length=30)



class Agendamento (models.Model):
    data_agendamento = models.IntegerField()
    horário_agendamento = models.IntegerField()
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    cadastro= models.ForeignKey(Cadastro,on_delete=models.CASCADE)



class Endereco (models.Model):
    rua  = models.CharField(max_length=40)
    número  = models.IntegerField(4) 
    cidade =  models.CharField()
    cep = models.IntegerField(8)



class Procedimento(models.Model):
    descricao = models.CharField(255) 
    data_proced = models.IntegerField()
    tempo_proced  = models.IntegerField()
    valor = models.CharField(max_length=5)



class Salao(models.Model):
    nome = models.CharField(15) 
    endereco = models.CharField(max_length=30)
    funcionario  = models.IntegerField()
    ativo = models.BooleanField(max_length= 1)
