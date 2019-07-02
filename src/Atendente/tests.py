from django.test import TestCase
from . import models
from . import methods


class ClientTest(TestCase):
    """
    Testes unitários do CRUD de Clientes
    """

    def setUp(self):
        """
        Inicializa as instâncias do BD.
        """
        models.Plan.objects.create(
            name='Plano A',
            price=1.99)
        
        models.Plan.objects.create(
            name='Plano B',
            price=3.49)
        
        methods.create_client(
            name='Usuário1',
            cpf='123.456.789-00',
            rg='12.345.678',
            birthday='1990-01-01',
            address='Rua',
            install_date='2019-01-02',
            install_hour='08:00:00',
            plan_id=1)

    def test_client_creation(self):
        """
        Testa Criação e Leitura.
        """
        client = models.Client.objects.get(id=1)

        self.assertEqual(client.person.name, 'Usuário1')
        self.assertEqual(client.person.cpf, '123.456.789-00')
        self.assertEqual(client.person.rg, '12.345.678')
        self.assertEqual(str(client.person.birthday), '1990-01-01')
        self.assertEqual(client.person.address, 'Rua')
        self.assertEqual(str(client.install_date.date), '2019-01-02')
        self.assertEqual(str(client.install_date.hour), '08:00:00')
        self.assertEqual(client.contract.plan.name, 'Plano A')

    def test_client_updating(self):
        """
        Testa Modificação.
        """
        client = models.Client.objects.get(id=1)

        methods.update_client(
            client=client,
            posted_plan_id=2,
            name='Usuário001',
            cpf='123.789.456-99',
            rg='99.678.345',
            birthday='1996-01-01',
            address='Casa')
        
        self.assertEqual(client.person.name, 'Usuário001')
        self.assertEqual(client.person.cpf, '123.789.456-99')
        self.assertEqual(client.person.rg, '99.678.345')
        self.assertEqual(str(client.person.birthday), '1996-01-01')
        self.assertEqual(client.person.address, 'Casa')
        self.assertEqual(str(client.install_date.date), '2019-01-02')
        self.assertEqual(str(client.install_date.hour), '08:00:00')
        self.assertEqual(client.contract.plan.name, 'Plano B')

    def test_client_deletion(self):
        """
        Testa Exclusão.
        """
        client = models.Client.objects.get(id=1)

        num_clients_before = len(models.Client.objects.all())
        methods.delete_client_subscription(client)
        num_clients_after = len(models.Client.objects.all())
        
        self.assertEqual(num_clients_before, 1)
        self.assertEqual(num_clients_after, 0)
