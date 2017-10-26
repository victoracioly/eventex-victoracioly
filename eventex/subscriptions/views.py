#coding utf-8

from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm, SomaForm, RaioxmovelForm
from django.http import HttpResponseRedirect

from eventex.subscriptions.models import Subscription


#Existem duas formas de requisicao: get e post. A get é quando voce usa o browser e o post é quando voce enviar um formulario
def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)
# Quando nao digitamos todos os campos ele inicia com as informacoes anteriores para voce nao ter que digitar tudo novamente.
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    # Send email
    _send_mail('Confirmacao de inscricao',
               settings.DEFAULT_FROM_EMAIL,
               form.cleaned_data['email'],
               'subscriptions/subscription_email.txt',
               form.cleaned_data)

    Subscription.objects.create(**form.cleaned_data)
    # Success feedback
    messages.success(request, 'Inscricao realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})

def list(request):
    inscritos = Subscription.objects.all()
    return render(request, 'subscriptions/subscription_list.html',
                  {'inscritos': inscritos})

def somaab(request):
    if request.method == 'POST':
        form = SomaForm(request.POST)

        if form.is_valid():
            a = int(form.cleaned_data['letraA'])
            b =int(form.cleaned_data['letraB'])
            c= a+b
            return render(request,'subscriptions/somaab.html',{'form': form, 'c':c}) #<-- Passando os valores
    else:
        form = SomaForm()
        return render(request,'subscriptions/somaab.html',{'form': form})

def raioxmovel(request):
    if request.method == 'POST':
        form = RaioxmovelForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['patrimonio']
            b = form.cleaned_data['setor']
            return render(request,'subscriptions/raioxmovel.html',{'form': form, 'a':a,'b':b})
    else:# Só tem dois métodos possíveis. Ou É POST ou é GET. O GET é quando o usuario entra na pagina. O POST é quando ela envia o formulario.
        form = RaioxmovelForm()
        return render(request,'subscriptions/raioxmovel.html',{'form': form})





















"""
def Add_Equipamento(request):
    if request.method =='POST':
        form = IdEquipamentoForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['equipamento']
            b = form.cleaned_data['patrimonio']
            c = form.cleaned_data['numerodeserie']
            return render(request,'subscriptions/adicionarequipamento.html',{'form': form, 'a':a,'b':b,'c':c})
    else:
        form = IdEquipamentoForm()
        return render(request,'subscriptions/adicionarequipamento.html',{'form': form})
"""

def _send_mail(subject,from_,to,template_name,context):
    body = render_to_string(template_name,context)
    mail.send_mail(subject, body, from_, [from_, to])
