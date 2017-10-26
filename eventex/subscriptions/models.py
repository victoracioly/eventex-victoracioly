#Tem que pensar em migracao como controle de versao do esquema do banco de dados

from django.db import models

class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF',max_length=11)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    equipamento = models.CharField('nome',max_length=100)
    patrimonio = models.CharField('nome',max_length=100)
    numerodeserie = models.CharField('nome',max_length=100)


    class Meta:
        verbose_name_plural = 'Inscrições'
        verbose_name = 'Inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

#class Setor(models.Model):
#    nome = models.CharField('nome',max_length=100)
"""
class Equipamento(models.Model):
    nome = models.CharField('nome',max_length=100)

class IdEquipamento (models.Model):
    equipamento = models.ForeignKey(Equipamento)
    patrimonio = models.CharField('nome',max_length=100)
    numerodeserie = models.CharField('nome',max_length=100)

"""
#class Emprestimo(models.Model):
#    equipamento = models.ForeignKey(Equipamento)
#    setor = models.ForeignKey(Setor)

#    data_inicio = models.DateTimeField(add)
#    data_fim = models.DateTimeField(add)
 #   usuario = models.U


