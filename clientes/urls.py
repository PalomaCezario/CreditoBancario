from django.urls import path  # type: ignore
from .views import home, consultar_credito

urlpatterns = [
    path('', home, name='home'),  # Página inicial
    path('consultar/', consultar_credito, name='consultar-credito'),
]
