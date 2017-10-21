from django.contrib import admin

from .models import Sca

class ScaAdmin(admin.ModelAdmin):
    list_display = ['setor', 'tipo', 'nome', 'data_venc', 'descricao']
    search_fields = ['nome', 'setor', 'tipo', 'descricao']

admin.site.register(Sca, ScaAdmin)
admin.site.site_header = 'Central de Comando e Operação - UNIT'
admin.site.site_title = 'Central de Comando e Operação - UNIT'
