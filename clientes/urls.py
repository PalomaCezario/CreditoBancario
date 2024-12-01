from django.urls import path, include
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, PredictView
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('new/', ClienteCreateView.as_view(), name='cliente-create'),
    path('<int:pk>/edit/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),
    path('predict/', PredictView.as_view(), name='predict'),  # Nova rota para predição
]
