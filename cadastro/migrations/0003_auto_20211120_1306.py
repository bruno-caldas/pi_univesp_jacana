# Generated by Django 3.2.6 on 2021-11-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_document_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspecieAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(help_text='Escreve a espécie do animal.', max_length=50, unique=True, verbose_name='Espécie')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='data_nascimento',
            field=models.DateTimeField(help_text='Coloque a data aproximada de nascimento do animal.', null=True, verbose_name='Nascimento'),
        ),
        migrations.AddField(
            model_name='document',
            name='porte',
            field=models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')], help_text='Escolha o porte do animal.', max_length=1, null=True, verbose_name='Porte'),
        ),
        migrations.AddField(
            model_name='document',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], help_text='Escolha o sexo do animal.', max_length=1, null=True, verbose_name='Sexo'),
        ),
        migrations.AddField(
            model_name='document',
            name='tipo',
            field=models.CharField(choices=[('D', 'Doméstico'), ('S', 'Selvagem')], help_text='Escolha o tipo do animal.', max_length=1, null=True, verbose_name='Tipo'),
        ),
    ]
