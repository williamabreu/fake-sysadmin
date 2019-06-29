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


def update_client(request, id):
    """
    Modifica dados do cliente cadastrados na base de dados (UPDATE).

    :param request: Requisição HTTP processada do Django
    :param id: Chave no banco de dados do cliente desejado
    :return: Página HTML de modificação do cliente
    """
    client = models.Client.objects.get(id=id)
    
    if request.method == 'GET':
        plans = models.Plan.objects.all()
        return render(request, 'site/update_client.html', context={'client': client, 'plans': plans})

    if request.method == 'POST':
        posted_plan_id = int(request.POST['plan'])
        
        if posted_plan_id != client.contract.plan.id:
            # Altera o plano de assinatura
            contract = models.Contract()
            contract.subscription_date = datetime.now()
            contract.plan = models.Plan.objects.get(id=posted_plan_id)
            contract.save()

            client.contract.delete()
            client.contract = contract
            client.save()
        
        client.person.name = request.POST['name']
        client.person.cpf = request.POST['cpf']
        client.person.rg = request.POST['rg']
        client.person.birthday = request.POST['birthday']
        client.person.address = request.POST['address']
        client.person.save()

        return redirect('update_client', id=id)
