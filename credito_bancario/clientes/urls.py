from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from .views import home, consultar_credito

urlpatterns = [
    path('', home, name='home'),  # Página inicial
    path('consultar/', consultar_credito, name='consultar-credito'),  # Página de consulta de crédito
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore
