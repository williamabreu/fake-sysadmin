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
        # Cria um plano
        models.Plan.objects.create(
            name='Plano A',
            price=1.99)
        
        # Cria outro plano
        models.Plan.objects.create(
            name='Plano B',
            price=3.49)
        
        # Cria um cliente
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
        num_persons = len(models.Person.objects.all())
        num_contract = len(models.Contract.objects.all())
        num_schedule = len(models.Schedule.objects.all())
        num_clients = len(models.Client.objects.all())

        # Verifica a quantidade de registros em tabelas:
        self.assertEqual(num_persons, 1)
        self.assertEqual(num_contract, 1)
        self.assertEqual(num_schedule, 1)
        self.assertEqual(num_clients, 1)

        # Verifica se os dados estão salvos corretamente:
        self.assertEqual(client.person.name, 'Usuário1')
        self.assertEqual(client.person.cpf, '123.456.789-00')
        self.assertEqual(client.person.rg, '12.345.678')
        self.assertEqual(str(client.person.birthday), '1990-01-01')
        self.assertEqual(client.person.address, 'Rua')
        self.assertEqual(str(client.install_date.date), '2019-01-02')
        self.assertEqual(str(client.install_date.hour), '08:00:00')
        self.assertEqual(client.contract.plan.name, 'Plano A')

        # Adiciona mais um cliente com a mesma instalação do outro
        # (não pode ser possível, pois instalação é única)
        methods.create_client(
            name='Usuário2',
            cpf='000.000.000-00',
            rg='00.000.000',
            birthday='1975-01-01',
            address='Rua',
            install_date='2019-01-02',
            install_hour='08:00:00',
            plan_id=2)
        
        # Não pode ter criado por causa da colisão do horário
        num_schedule = len(models.Schedule.objects.all())
        self.assertEqual(num_schedule, 1)

    def test_client_updating(self):
        """
        Testa Modificação.
        """
        client = models.Client.objects.get(id=1)

        # Modifca os dados do cliente
        methods.update_client(
            client=client,
            posted_plan_id=2,
            name='Usuário001',
            cpf='123.789.456-99',
            rg='99.678.345',
            birthday='1996-01-01',
            address='Casa')
        
        # Verifica se os dados foram alterados corretamente:
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

        # Exclui e faz contagem no banco de dados para conferir
        num_clients_before = len(models.Client.objects.all())
        methods.delete_client_subscription(client)
        num_clients_after = len(models.Client.objects.all())
        
        # Verifica se realmente foi excluído 1 registro
        self.assertEqual(num_clients_before, 1)
        self.assertEqual(num_clients_after, 0)

        num_persons = len(models.Person.objects.all())
        num_contract = len(models.Contract.objects.all())
        num_schedule = len(models.Schedule.objects.all())

        # Verifica se outras tabelas também foram alteradas:
        self.assertEqual(num_persons, 0)
        self.assertEqual(num_contract, 0)
        self.assertEqual(num_schedule, 0)
