from django.db import models

class Setor(models.Model):
    setor = models.CharField('Setor', max_length=100)
    descricao = models.TextField('Descrição', blank=True)

SETOR_LISTA = [(s.setor, s.setor) for s in Setor.objects.all().order_by('setor')]

class Tipo(models.Model):
    tipo = models.CharField('Tipo', max_length=100)
    descricao = models.TextField('Descrição', blank=True)

TIPO_LISTA = [(s.tipo, s.tipo) for s in Tipo.objects.all().order_by('tipo')]

class Sca(models.Model):
    setor = models.CharField('Setor', max_length=100, choices=SETOR_LISTA)
    tipo = models.CharField('Tipo', max_length=100, choices=TIPO_LISTA)
    id_chamado = models.CharField('ID Chamado', max_length=12, null=True)
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True)
    data_venc = models.DateTimeField('Data Vencimento', null=True, blank=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    status = models.BooleanField('Status (Ativo=Acessou)', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Acesso'
