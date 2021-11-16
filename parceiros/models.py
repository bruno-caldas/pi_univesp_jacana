from django.db import models
from django.db.models import base

# Create your models here.
class Parceiros(models.Model):
    nome_parceiro = models.CharField(max_length=100,null=False,blank=False,unique=True,verbose_name='Parceiro',help_text='Escreve o nome do Parceiro.')
    descricao_parceiro = models.TextField(null=False,blank=False,unique=True,verbose_name='Resumo sobre o Parceiros',help_text='Descreva um resumo sobre o ramo do parceiro')
    site_parceiro = models.CharField(max_length=250,null=False,blank=False,unique=True,verbose_name='Site',help_text='Insira o site do parceiro')
    class Meta:
        db_table = 'parceiro'
        ordering = ['nome_parceiro']
    def __str__(self):
        return self.nome_parceiro