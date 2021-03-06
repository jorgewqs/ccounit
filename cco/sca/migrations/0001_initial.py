# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=100, verbose_name='Setor')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('status', models.BooleanField(verbose_name='Status (Ativo=Acessou)')),
                ('data_venc', models.DateTimeField(blank=True, null=True, verbose_name='Data Vencimento')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
