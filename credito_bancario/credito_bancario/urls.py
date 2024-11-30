from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from django.shortcuts import redirect  # type: ignore

urlpatterns = [
    # Interface administrativa
    path('admin/', admin.site.urls),  # Acesso ao admin Django
    
    # Interface para clientes
    path('clientes/', include('clientes.urls')),  # URLs específicas do app "clientes"

    # Redirecionamento da raiz para a página inicial
    path('', lambda request: redirect('home'), name='root'),  # Redireciona para a página inicial dos clientes
]
