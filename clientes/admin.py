from django.contrib import admin # type: ignore
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('sexo', 'regiao', 'estado_civil', 'numero_filhos', 'propriedade', 'educacao', 'vinculo_empregaticio', 'fonte_renda', 'marker')
    list_filter = ('sexo', 'regiao', 'estado_civil', 'numero_filhos', 'propriedade', 'educacao', 'vinculo_empregaticio', 'fonte_renda', 'marker')
    search_fields = ('sexo', 'regiao', 'estado_civil')

