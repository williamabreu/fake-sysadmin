"""
Controles do CRUD do Atendente.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models


def create_client(request):
    """
    Cadastra um Cliente na base de dados (CREATE).

    :param request: Requisição HTTP processada do Django
    :return: Página HTML de cadastro do cliente
    """
    if request.method == 'GET':
        plans = models.Plan.objects.all()
        return render(request, 'site/create_client.html', context={'plans': plans})
    
    if request.method == 'POST':
        person = models.Person()
        person.name = request.POST['name']
        person.cpf = request.POST['cpf']
        person.rg = request.POST['rg']
        person.birthday = request.POST['birthday']
        person.address = request.POST['address']
        person.save()
        
        install_date = models.Schedule()
        install_date.date = request.POST['install_date']
        install_date.hour = request.POST['install_hour']
        install_date.save()
        
        contract = models.Contract()
        contract.subscription_date = datetime.now()
        contract.plan = models.Plan.objects.get(id=int(request.POST['plan']))
        contract.save()

        client = models.Client()
        client.person = person
        client.install_date = install_date
        client.contract = contract
        client.save()
        
        return redirect('create_client')


def list_all_clients(request):
    """
    Lista todos os Clientes cadastrados na base de dados (READ).

    :param request: Requisição HTTP processada do Django
    :return: Página HTML de listagem de clientes
    """
    if request.method == 'GET':
        clients = models.Client.objects.all()
        return render(request, 'site/list_all_clients.html', context={'clients': clients})
