from django.db import models
from datetime import datetime

# Create your models here.
class Evento(models.Model):
    nome_evento = models.CharField(blank=False,null=False,unique=True,max_length=100,verbose_name='Nome do Evento')
    descricao_evento = models.TextField(blank=False,null=False,unique=True,verbose_name='Descrição do Evento')
    local_evento = models.CharField(max_length=150,verbose_name='Local do Evento')
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
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