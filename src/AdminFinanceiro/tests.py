from django.test import TestCase
from . import models


class PlanTest(TestCase):
    """
    Testes unitários do CRUD de Planos
    """

    def setUp(self):
        """
        Inicializa as instâncias do BD.
        """
        plan1 = models.Plan()
        plan1.name = 'Testando'
        plan1.price = 12.34
        plan1.save()

        plan2 = models.Plan()
        plan2.name = 'Testando ABC'
        plan2.price = 150.00
        plan2.save()

    def test_plan_creation(self):
        """
        Testa Criação e Leitura.
        """
        plan = models.Plan.objects.get(name='Testando')
        self.assertEqual(plan.name, 'Testando')
        self.assertEqual(float(plan.price), 12.34)

    def test_plan_updating(self):
        """
        Testa Modificação.
        """
        plan = models.Plan.objects.get(name='Testando')
        plan.name = 'Novo Nome'
        plan.price = 0.99
        plan.save()
        self.assertEqual(plan.name, 'Novo Nome')
        self.assertEqual(float(plan.price), 0.99)

    def test_plan_deletion(self):
        """
        Testa Exclusão.
        """
        listing = models.Plan.objects.filter(name='Testando ABC')
        self.assertEqual(len(listing), 1)
        models.Plan.objects.get(name='Testando ABC').delete()
        listing = models.Plan.objects.filter(name='Testando ABC')
        self.assertEqual(len(listing), 0)
