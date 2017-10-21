# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvrscan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dvrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade_dvr', models.CharField(max_length=100, verbose_name='Unidade')),
                ('name_dvr', models.CharField(max_length=100, verbose_name='Nome')),
                ('local_dvr', models.CharField(max_length=100, verbose_name='Local')),
                ('ip_dvr', models.GenericIPAddressField(null=True, verbose_name='IPv4 address')),
                ('descricao_dvr', models.TextField(blank=True, verbose_name='Descrição')),
                ('status_dvr', models.BooleanField(verbose_name='Status')),
                ('data_atualizacao_dvr', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.DeleteModel(
            name='Dvr',
        ),
    ]
