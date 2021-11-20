# Generated by Django 3.2.5 on 2021-11-20 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20211120_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='especie',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.especieanimal'),
        ),
        migrations.AddField(
            model_name='document',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
