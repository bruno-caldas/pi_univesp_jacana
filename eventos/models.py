from django.db import models
from datetime import datetime

from parceiros.models import Parceiros

# Create your models here.
class Evento(models.Model):
    nome_evento = models.CharField(blank=False,null=False,unique=True,max_length=100,verbose_name='Nome do Evento',help_text='Insira o nome do evento.')
    descricao_evento = models.TextField(blank=False,null=False,unique=True,verbose_name='Descrição do Evento',help_text='Faça uma breve descrição sobre o evento.')
    local_evento = models.CharField(max_length=150,verbose_name='Local do Evento',help_text='Exemplo: Rua, número, Bairro, CEP, Município, UF')
    data_evento = models.DateTimeField(verbose_name='Data do Evento',help_text='Data de realização do evento.')
    parceiros = models.ManyToManyField(Parceiros,verbose_name='Parceiros',help_text='Insira os parceiros do evento.')
    class Meta: #nome definido da tabela no DB
        db_table = 'evento'
    def __str__(self): #correção para admin.py na aparecer como object
        return self.nome_evento
    def get_data_evento(self): #função para retornar a data formatada
        return self.data_evento.strftime('%d/%m/%Y %H:%M')
    def get_evento_vencido(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False