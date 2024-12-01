from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="API de Clientes para Concessão de Empréstimos",
        default_version='v1',
        description="Documentação da API para gerenciamento de clientes e concessão de empréstimos",
        contact=openapi.Contact(email="limmwillams@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),  # Inclui as rotas de clientes
    path('', lambda request: redirect('cliente-list')),  # Redireciona para a lista de clientes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
