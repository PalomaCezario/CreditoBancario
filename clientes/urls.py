from django.urls import path
from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from .views import home, consultar_credito
from .views import PredictView  
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('', home, name='home'),  # Página inicial
    path('consultar/', consultar_credito, name='consultar-credito'),  # Página de consulta de crédito
    path('predict/', PredictView.as_view(), name='predict'),  # Defina a URL da view de predição
    path('clientes/', ClienteListView.as_view(), name='clientes-list'),  # GET para listar clientes e POST para criar cliente
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='clientes-detail'),  # GET para detalhes de um cliente específico
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='clientes-update'),  # PUT para atualizar cliente
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='clientes-delete'),  # DELETE para excluir cliente
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore
