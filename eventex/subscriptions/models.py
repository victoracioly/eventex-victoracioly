#Tem que pensar em migracao como controle de versao do esquema do banco de dados

from django.db import models

class Subscription(models.Model):
    name=models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


