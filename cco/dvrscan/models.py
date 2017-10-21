from django.db import models

class Dvr(models.Model):

	unidade_dvr = models.CharField('Unidade', max_length=100)
	name_dvr = models.CharField('Nome', max_length=100)
	local_dvr = models.CharField('Local', max_length=100)
	ip_dvr = models.GenericIPAddressField('IPv4 address', max_length=15, null=True)
	descricao_dvr = models.TextField('Descrição', blank=True)
	status_dvr = models.BooleanField('Status (Ativo=ONLINE)', blank=True)
    #data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
	data_atualizacao_dvr = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.name_dvr

	class Meta:
		ordering = ['name_dvr']
		verbose_name = 'Cadastro de DVR'
