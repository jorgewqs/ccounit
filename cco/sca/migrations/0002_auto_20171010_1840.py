# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sca',
            options={'ordering': ['nome'], 'verbose_name': 'Controle de Acesso'},
        ),
        migrations.AddField(
            model_name='sca',
            name='id_chamado',
            field=models.CharField(max_length=12, null=True, verbose_name='ID Chamado'),
        ),
    ]