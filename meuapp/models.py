from django.db import models

class Cachorro(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    idade = models.IntegerField()
    foto = models.ImageField(upload_to='ftsAnimais/', null=True, blank=True)
    descricao = models.TextField(blank=True)
    meta = models.FloatField(default=0.0)
    arrecadado = models.FloatField(default=0.0)
    adotado = models.BooleanField(default=False)
    adotadoPor = models.CharField(max_length=100, null=True, blank=True)
    historia = models.CharField(max_length=1000, null=True, blank=True)
    diaAdocao = models.DateField(null=True, blank=True)
    porte = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome
