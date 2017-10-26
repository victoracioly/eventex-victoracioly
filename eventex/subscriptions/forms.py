#coding utf-8

from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Telefone')
    equipamento = forms.CharField(label='Equipamento')
    patrimonio = forms.IntegerField(label='Número de Patrimônio')
    numerodeserie = forms.CharField(label='Número de Serie')


"""
class IdEquipamentoForm(forms.Form):
    equipamento = forms.CharField(label='Equipamento')
    patrimonio = forms.IntegerField(label='Número de Patrimônio')
    numerodeserie = forms.CharField(label='Número de Serie')
"""



class SomaForm (forms.Form):
    letraA= forms.IntegerField(label='A')
    letraB= forms.IntegerField(label='B')

class RaioxmovelForm (forms.Form):
    patrimonio = forms.IntegerField(label='Patrimônio')
    setor = forms.CharField(label='Setor')



