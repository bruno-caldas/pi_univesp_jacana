from django.db import models
from django.contrib import admin
from django.utils import timezone
from djrichtextfield.models import RichTextField
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class EspecieAnimal(models.Model):
    especie = models.CharField(max_length=50,null=False,blank=False,unique=True,verbose_name='Espécie',help_text='Escreve a espécie do animal.')
    class Meta:
        db_table = 'especie' #nome definido da tabela no DB
        ordering = ['especie']
    def __str__(self): #correção para admin.py na aparecer como object
        return self.especie

class Document(models.Model):
    SEXO_ANIMAL = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        )
    TIPO_ANIMAL = (
        ('D', 'Doméstico'),
        ('S', 'Selvagem'),
        )
    PORTE_ANIMAL = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
        )
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    # docfile = models.FileField(upload_to='cadastro/media')
    docfile = models.FileField(upload_to='cadastro/media/%Y_%m_%d')
    nome_cachorro = models.CharField(max_length=30,verbose_name='Nome',help_text='Insira o nome do animal.')
    descricao = RichTextField(default='')
    sexo = models.CharField(null=True,max_length=1,choices=SEXO_ANIMAL, verbose_name='Sexo',help_text='Escolha o sexo do animal.')
    tipo = models.CharField(null=True,max_length=1,choices=TIPO_ANIMAL, verbose_name='Tipo',help_text='Escolha o tipo do animal.')
    porte = models.CharField(null=True,max_length=1,choices=PORTE_ANIMAL, verbose_name='Porte',help_text='Escolha o porte do animal.')
    data_nascimento = models.DateTimeField(null=True,verbose_name='Nascimento',help_text='Coloque a data aproximada de nascimento do animal.')
    especie = models.ForeignKey(EspecieAnimal,on_delete=models.CASCADE, blank=True, null=True, default=2)
    # url = models.URLField(null=True,max_length=200)
    class Meta:
        db_table = 'mural_fofura' #nome definido da tabela no DB
        ordering = ['nome_cachorro','data_nascimento','tipo','porte']
    def __str__(self): #correção para admin.py na aparecer como object
        return self.nome_cachorro
    # pip install boto3 django-storages
