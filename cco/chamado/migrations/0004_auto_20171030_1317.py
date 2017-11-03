# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0003_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='id_chamado',
            field=models.CharField(max_length=14, null=True, verbose_name='ID Chamado'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='setor',
            field=models.CharField(choices=[('Assessoria Jurídica', 'Assessoria Jurídica'), ('Setor de Almoxarifado', 'Setor de Almoxarifado')], max_length=100, verbose_name='Setor'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='tipo',
            field=models.CharField(choices=[('PC TRAVANDO', 'PC TRAVANDO')], max_length=100, verbose_name='Tipo'),
        ),
    ]
