from django.urls import path
from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from .views import home, consultar_credito
from .views import PredictView  
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from django.urls import path, re_path
from django.views.generic import TemplateView
from clientes.dash_app import app as dash_app  # Verifique se você está importando corretamente

urlpatterns = [
    path('', home, name='home'),  # Página inicial
    path('consultar/', consultar_credito, name='consultar-credito'),  # Página de consulta de crédito
    path('predict/', PredictView.as_view(), name='predict'),  # Defina a URL da view de predição
    path('clientes/', ClienteListView.as_view(), name='clientes-list'),  # GET para listar clientes e POST para criar cliente
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='clientes-detail'),  # GET para detalhes de um cliente específico
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='clientes-update'),  # PUT para atualizar cliente
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='clientes-delete'),  # DELETE para excluir cliente
    re_path(r'^dash/', dash_app.server.wsgi_app, name='dash'),  # Adicione um nome para a URL
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])