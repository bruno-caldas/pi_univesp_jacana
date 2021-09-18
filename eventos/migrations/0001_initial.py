# Generated by Django 3.2.6 on 2021-09-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_evento', models.CharField(max_length=100, unique=True, verbose_name='Nome do Evento')),
                ('descricao_evento', models.TextField(unique=True, verbose_name='Descrição do Evento')),
                ('local_evento', models.CharField(max_length=150, verbose_name='Local do Evento')),
                ('data_evento', models.DateTimeField(verbose_name='Data do Evento')),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]
