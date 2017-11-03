from django.contrib import admin

from .models import Chamado

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ['id_chamado', 'setor', 'tipo', 'nome', 'descricao', 'status']
    search_fields = ['id_chamado', 'nome', 'setor', 'tipo', 'descricao', 'status']
    readonly_fields = ['id_chamado']

admin.site.register(Chamado, ChamadoAdmin)
admin.site.site_header = 'CCO - UNIT'
admin.site.site_title = 'Central de Comando e Operação - UNIT'
