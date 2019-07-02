"""
Controles do CRUD do Atendente.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import methods


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
        methods.create_client(
            request.POST['name'],
            request.POST['cpf'],
            request.POST['rg'],
            request.POST['birthday'],
            request.POST['address'],
            request.POST['install_date'],
            request.POST['install_hour'],
            int(request.POST['plan']))

        return redirect('create_client')


def list_all_clients(request):
    """
    Lista todos os Clientes cadastrados na base de dados (READ).

    :param request: Requisição HTTP processada do Django
    :return: Página HTML de listagem de clientes
    """
    if request.method == 'GET':
        clients = methods.list_all_clients()
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
        methods.update_client(
            client,
            int(request.POST['plan']),
            request.POST['name'],
            request.POST['cpf'],
            request.POST['rg'],
            request.POST['birthday'],
            request.POST['address'])

        return redirect('update_client', id=id)


def delete_client_subscription(request, id):
    """
    Cancela a assinatura de um cliente (DELETE).

    :param request: Requisição HTTP processada do Django
    :param id: Chave no banco de dados do cliente desejado
    :return: Resposta HTTP de conclusão da operação
    """
    if request.method == 'GET':
        client = models.Client.objects.get(id=id)
        methods.delete_client_subscription(client)
        return HttpResponse(f'Assinatura do cliente {client.person.name} cancelada.')
