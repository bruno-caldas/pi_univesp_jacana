# Generated by Django 3.2.5 on 2021-11-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_alter_document_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
