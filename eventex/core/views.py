# coding=utf-8
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def novo(request):
    pessoa = request.GET['nome']

    frutas = ['banana', 'maça', 'salada mista']
    print(pessoa)
    return render(request, 'novo.html', { 'pessoa': pessoa, 'frutas': frutas })

def outronovo(request):
    return render(request,'outro_novo.html')

