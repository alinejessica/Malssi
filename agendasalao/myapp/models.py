from django.db import models

class Funcionario(models.Model) :
    cpf = models.CharField (max_length=11)
    procedimento = models.CharField(max_length=20)
    ativo = models.BooleanField(max_length= 1) 
    gerente = models.BooleanField(max_length=1)



class Cadastro (models.Model):
    nome = models.CharField(max_length=10)
    sobrenome = models.CharField(max_length=50) 
    email = models.CharField(max_length=30) 
    senha = models.CharField(max_length=10) 
    telefone =  models.IntegerField(max_length=11) 
    data_de_nasc = models.IntegerField(max_length=8)
    endereco = models.CharField(max_length=30)



class Agendamento (models.Model):
    data_agendamento = models.IntegerField(max_length=6)
    horário_agendamento = models.IntegerField(max_length=4)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    cadastro= models.ForeignKey(Cadastro,on_delete=models.CASCADE)



class Endereco (models.Model):
    rua  = models.CharField(max_length=40)
    número  = models.IntegerField(max_length=40) 
    cidade =  models.CharField(max_length=40)
    cep = models.IntegerField(max_length=11)



class Procedimento(models.Model):
    descricao = models.CharField(max_length=40) 
    data_proced = models.IntegerField(max_length=4)
    tempo_proced  = models.IntegerField(max_length=4)
    valor = models.CharField(max_length=5)



class Salao(models.Model):
    nome = models.CharField(max_length=45) 
    endereco = models.CharField(max_length=30)
    funcionario  = models.IntegerField(max_length=5)
    ativo = models.BooleanField(max_length= 1)
