from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT


# Create your models here.


class Cupon(models.Model):
    nome = models.CharField(max_length=200)
    fone_celular = models.CharField(max_length=20)
    fone_whatsapp = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    obs = models.TextField(max_length=400, blank=True)  
    cupon = models.CharField(max_length=20)
    data_cadastro = models.DateField()

    def __str__(self):
        return self.nome

class Leads(models.Model):
    UF = (
        ('RN','RN'),
    )
    CIDADES = (
        ('1','Felipe Guerra'),
        ('2','Gov. Dix-Sept Rosado')
    )
    nome = models.CharField(max_length=200)
    fone_celular = models.CharField(max_length=20)
    fone_whatsapp = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    cidade = models.CharField(max_length=200, choices=CIDADES)
    uf = models.CharField(max_length=2, choices=UF)
    obs = models.TextField(max_length=400, blank=True)  
    cupon = models.ForeignKey(Cupon, on_delete=RESTRICT, null=True)
    data_cadastro = models.DateField()
    cliente_ativado = models.BooleanField(default=False)
