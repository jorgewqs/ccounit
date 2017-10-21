from django.db import models

class Sca(models.Model):

    setor = models.CharField('Setor', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)
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
