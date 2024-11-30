from django.shortcuts import render  # type: ignore
from .forms import ConsultaCreditoForm

def home(request):
    """
    Renderiza a página inicial do app 'clientes'.
    """
    return render(request, 'clientes/home.html')  # Certifique-se de que o template existe

def consultar_credito(request):
    """
    Renderiza a página de consulta de crédito com o formulário baseado no ModelForm.
    """
    form = ConsultaCreditoForm()  # Inicializa o formulário vazio
    resultado = None

    if request.method == 'POST':
        form = ConsultaCreditoForm(request.POST)
        if form.is_valid():
            # Salve ou processe os dados aqui
            cliente = form.save(commit=False)  # Se quiser salvar, use commit=True
            resultado = f"Consulta realizada com sucesso para {cliente.nome}!"

    return render(request, 'clientes/consultar_credito.html', {'form': form, 'resultado': resultado})
