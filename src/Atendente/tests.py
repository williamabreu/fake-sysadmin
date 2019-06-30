from django.test import TestCase
from . import models


class ClientTest(TestCase):
    """
    Testes unitários do CRUD de Clientes
    """

    def setUp(self):
        """
        Inicializa as instâncias do BD.
        """
        models.Plan.objects.create(
            name='PlanoA',
            price=1.99)

        models.Person.objects.create(
            name='Usuário1',
            cpf='123.456.789-00',
            rg='12.345.678',
            birthday='1990-01-01',
            address='Rua')

        models.Schedule.objects.create(
            date='2019-01-02',
            hour='08:00')

        models.Contract.objects.create(
            subscription_date='2018-12-30',
            plan=models.Plan.objects.get(name='PlanoA'))

        models.Client.objects.create(
            person=models.Person.objects.get(name='Usuário1'),
            install_date=models.Schedule.objects.get(date='2019-01-02'),
            contract=models.Contract.objects.get(plan__name='PlanoA'))

    def test_client_creation(self):
        """
        Testa Criação e Leitura.
        """
        client = models.Client.objects.get(person__name='Usuário1')
        self.assertEqual(client.person.cpf, '123.456.789-00')
        self.assertEqual(str(client.install_date.date), '2019-01-02')

    def test_client_updating(self):
        """
        Testa Modificação.
        """
        pass

    def test_client_deletion(self):
        """
        Testa Exclusão.
        """
        pass
