from django.db import models
from django.db.models import Avg


class ValorNutricional(models.Model):
    nome = models.CharField(max_length=256)
    calorias = models.FloatField()

class Ingrediente(models.Model):
    nome = models.CharField(max_length=256)
    unidade = models.CharField(max_length=256)
    descricao = models.TextField()
    valor_nutricional = models.OneToOneField(ValorNutricional, on_delete=models.SET_NULL, null=True)

class Receita(models.Model):
    nome = models.CharField(max_length=256)
    ingredientes = models.ManyToManyField(Ingrediente)

    def favoritar(self):
        return

class Avaliacao(models.Model):
    estrelas = models.IntegerField()
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, null=True)

    def avaliar(self, avaliacao):
        self.estrelas = avaliacao
        return self.estrelas
    
    def media_estrelas(self):
        return Avaliacao.objects.filter(receita=self.receita).aggregate(Avg('estrelas'))['estrelas__avg']
