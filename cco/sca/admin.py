from django.contrib import admin

from .models import Sca

class ScaAdmin(admin.ModelAdmin):
    list_display = ['setor', 'tipo', 'nome', 'data_venc', 'descricao', 'status']
    search_fields = ['nome', 'setor', 'tipo', 'descricao']
    list_per_page = 50
    date_hierarchy = 'data_criacao'
    list_filter = ['setor', 'tipo', 'status']

admin.site.register(Sca, ScaAdmin)
admin.site.site_header = 'Central de Comando e Operação - UNIT'
admin.site.site_title = 'Central de Comando e Operação - UNIT'
