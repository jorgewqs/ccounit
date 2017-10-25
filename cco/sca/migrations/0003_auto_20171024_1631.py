# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sca', '0002_auto_20171010_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=10, verbose_name='Setor')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
        ),
        migrations.AlterModelOptions(
            name='sca',
            options={'ordering': ['nome'], 'verbose_name': 'Acesso'},
        ),
    ]