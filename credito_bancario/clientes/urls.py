from django.urls import path # type: ignore
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('new/', ClienteCreateView.as_view(), name='cliente-create'),
    path('<int:pk>/edit/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),
]
