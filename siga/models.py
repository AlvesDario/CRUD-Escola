from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length = 30)
    matricula = models.ForeignKey('Matricula', on_delete = models.CASCADE)
    senha = models.CharField(max_length = 6, default = "123456")
    def __str__(self):
        return self.nome

class Matricula(models.Model):
    codigo = models.IntegerField()
    disciplina = models.ForeignKey('Disciplina', on_delete = models.CASCADE)
    notaf = models.FloatField()
    faltas = models.IntegerField()
    def __str__(self):
        return f'{self.codigo} <-> {self.disciplina.titulo}'

class Alocacao(models.Model):
    ano = models.DateTimeField()
    carga = models.FloatField()
    horario = models.CharField(max_length = 14)
    professor = models.ForeignKey('Professor', on_delete = models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.professor.nome} <-> {self.disciplina.titulo}'

class Disciplina(models.Model):
    titulo = models.CharField(max_length = 20)
    codigo = models.IntegerField()
    def __str__(self):
        return self.titulo

class Professor(models.Model):
    nome = models.CharField(max_length = 30)
    endereco = models.CharField(max_length = 50)
    titulacao = models.CharField(max_length = 20)
    nfunc = models.CharField(max_length = 20)
    fone = models.CharField(max_length = 11)
    def __str__(self):
        return self.nome
