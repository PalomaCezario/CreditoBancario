from django.shortcuts import render  
from .forms import ConsultaCreditoForm
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ClienteSerializer
from .models import Cliente
import numpy as np
import keras
from drf_yasg.utils import swagger_auto_schema


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



# Carregar o modelo ao iniciar
MODEL_PATH = 'C:/Users/limmw/OneDrive/Área de Trabalho/back-ia/creditobancario/model/modelo_treinado_cd.h5'
model = keras.models.load_model(MODEL_PATH)

# Views com documentação Swagger
class ClienteListView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_description="Listar todos os clientes",
        responses={
            200: ClienteSerializer(many=True),
            401: "Unauthorized - Usuário não autenticado",
            403: "Forbidden - Permissão negada"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ClienteDetailView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_description="Obter detalhes de um cliente específico",
        responses={
            200: ClienteSerializer,
            401: "Unauthorized - Usuário não autenticado",
            404: "Not Found - Cliente não encontrado",
            403: "Forbidden - Permissão negada"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_description="Criar um novo cliente",
        responses={
            201: ClienteSerializer,
            400: "Bad Request - Dados inválidos",
            401: "Unauthorized - Usuário não autenticado",
            403: "Forbidden - Permissão negada"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ClienteUpdateView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_description="Atualizar um cliente existente",
        responses={
            200: ClienteSerializer,
            400: "Bad Request - Dados inválidos",
            404: "Not Found - Cliente não encontrado",
            401: "Unauthorized - Usuário não autenticado",
            403: "Forbidden - Permissão negada"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class ClienteDeleteView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_description="Excluir um cliente",
        responses={
            204: "No Content - Cliente excluído com sucesso",
            404: "Not Found - Cliente não encontrado",
            401: "Unauthorized - Usuário não autenticado",
            403: "Forbidden - Permissão negada"
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class PredictView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(operation_description="Realizar predição com o modelo treinado")
    def post(self, request, *args, **kwargs):
        try:
            if model is None:
                return Response({'error': 'Modelo não carregado corretamente.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            data = request.data
            if not data or 'inputs' not in data:
                return Response({'error': 'Dados inválidos ou ausentes.'}, status=status.HTTP_400_BAD_REQUEST)

            input_data = np.array(data['inputs'])
            if input_data.shape[0] != 16:
                return Response({'error': f"Número incorreto de características. Esperado 16, mas recebido {input_data.shape[0]}."}, status=status.HTTP_400_BAD_REQUEST)

            input_data = input_data.reshape(1, -1)
            predictions = model.predict(input_data)

            response = {'prediction': predictions.tolist()}
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f"Erro ao processar: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
