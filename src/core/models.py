from django.db import models

# Create your models here.

class Plan(models.Model):
    plan_name = models.CharField('Nome do plano', max_length=32, default="")
    price = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0.0)