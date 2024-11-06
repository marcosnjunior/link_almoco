from django.db import models


class Registro(models.Model):
    
    CONTRA = [
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
    ]
    
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contra = models.CharField(max_length=200, choices=CONTRA, verbose_name="Contra turno")
    data_almoco = models.DateField()
    
    def __str__(self):
        return self.nome
    
    
class Configuracao(models.Model):
    
    nome = models.CharField(max_length=50)
    aberto = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
    
    
