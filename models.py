from django.db import models

class Assistido(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=20, unique=True)

class EvolucaoClinica(models.Model):
    assistido = models.ForeignKey(Assistido, on_delete=models.CASCADE, related_name='evolucoes')
    especialidade = models.CharField(max_length=100)
    parecer_tecnico = models.TextField()
    meta_pdi_cumprida = models.BooleanField(default=False)
    data_registro = models.DateTimeField(auto_now_add=True)
