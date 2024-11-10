from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # type: ignore
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'  # para acessar a lista de clientes no template

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'  # para acessar o cliente específico no template

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente-list')  # redireciona após criação

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente-list')  # redireciona após atualização

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')  # redireciona após exclusão
