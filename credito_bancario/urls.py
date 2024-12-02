from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from django.shortcuts import redirect  # type: ignore
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="API de Crédito Bancário",
      default_version='v1',
      description="Documentação da API de Crédito Bancário",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="limmwillams@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('clientes/', include('clientes.urls')),  # URLs específicas do app "clientes"
    path('', lambda request: redirect('home'), name='root'),  # Redireciona para a página inicial dos clientes
    path('api/', include('clientes.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
