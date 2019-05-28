from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Aluno)
admin.site.register(models.Matricula)
admin.site.register(models.Professor)
admin.site.register(models.Disciplina)
admin.site.register(models.Alocacao)