# Generated by Django 2.2.2 on 2019-06-28 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminFinanceiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32, verbose_name='Nome')),
                ('cpf', models.CharField(default='', max_length=14, verbose_name='CPF')),
                ('rg', models.CharField(default='', max_length=14, verbose_name='RG')),
                ('birthday', models.DateField(verbose_name='Data de Nascimento')),
                ('address', models.CharField(default='', max_length=64, verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('hour', models.TimeField(verbose_name='Hora')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_date', models.DateField(verbose_name='Data de Assinatura')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AdminFinanceiro.Plan', verbose_name='Plano')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atendente.Contract', verbose_name='Contrato')),
                ('install_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atendente.Schedule', verbose_name='Data de Instalação')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atendente.Person', verbose_name='Pessoa')),
            ],
        ),
    ]
