# Generated by Django 3.2.6 on 2021-09-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_parceiro', models.CharField(help_text='Escreve o nome do Parceiro.', max_length=100, unique=True, verbose_name='Parceiro')),
                ('descricao_parceiro', models.TextField(help_text='Descreva um resumo sobre o ramo do parceiro', unique=True, verbose_name='Resumo sobre o Parceiros')),
                ('site_parceiro', models.CharField(help_text='Insira o site do parceiro', max_length=250, unique=True, verbose_name='Site')),
            ],
            options={
                'db_table': 'parceiro',
            },
        ),
    ]
