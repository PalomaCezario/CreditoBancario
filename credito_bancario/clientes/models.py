from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    regiao = models.CharField(max_length=50)
    escolaridade = models.CharField(max_length=50)
    # Defina mais campos com base nas colunas que você analisou

    def __str__(self):
        return self.nome

