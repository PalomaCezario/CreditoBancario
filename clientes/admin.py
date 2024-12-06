from django.contrib import admin  # type: ignore
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Exibição principal na lista de clientes no admin
    list_display = (
        'nome', 
        'email', 
        'sexo', 
        'regiao', 
        'estado_civil', 
        'numero_filhos', 
        'propriedade', 
        'educacao', 
        'vinculo_empregaticio', 
        'fonte_renda', 
        'resultado_credito'
    )

    # Filtros laterais para facilitar a segmentação
    list_filter = (
        'sexo', 
        'regiao', 
        'estado_civil', 
        'numero_filhos', 
        'propriedade', 
        'educacao', 
        'vinculo_empregaticio', 
        'fonte_renda', 
    )
    # Campos para busca rápida
    search_fields = ('nome', 'email', 'sexo', 'regiao', 'estado_civil')

    # Organização e leitura nos formulários do admin
    fieldsets = (
        ("Informações Pessoais", {
            'fields': ('nome', 'email', 'sexo', 'estado_civil', 'numero_filhos')
        }),
        ("Informações Residenciais", {
            'fields': ('regiao', 'propriedade')
        }),
        ("Informações Educacionais e Profissionais", {
            'fields': ('educacao', 'vinculo_empregaticio', 'fonte_renda')
        }),
       
    )

