from django.contrib import admin

from .models import Dvr

class DvrAdmin(admin.ModelAdmin):
    list_display = ['name_dvr', 'unidade_dvr', 'local_dvr', 'ip_dvr']
    search_fields = ['name_dvr', 'local_dvr', 'unidade_dvr']

admin.site.register(Dvr, DvrAdmin)
admin.site.site_header = 'Central de Comando e Operação - UNIT'
admin.site.site_title = 'Central de Comando e Operação - UNIT'
