import numpy as np
import keras
import joblib
import pandas as pd
from django.shortcuts import render  
from .forms import ConsultaCreditoForm
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ClienteSerializer
from .models import Cliente
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny 
from .forms import ConsultaCreditoForm
from tensorflow.keras.models import load_model
from joblib import load
from sklearn.preprocessing import LabelEncoder

scaler = load('C:/Users/limmw/OneDrive/Área de Trabalho/back-ia/creditobancario/model/scaler.pkl')
label_encoder = joblib.load('C:/Users/limmw/OneDrive/Área de Trabalho/back-ia/creditobancario/model/label_encoder.pkl')

# Carregar o modelo de IA

modelo = load_model('C:/Users/limmw/OneDrive/Área de Trabalho/back-ia/creditobancario/model/modelo_treinado_cd.h5')


def validar_dados(dados):
    if not isinstance(dados, np.ndarray):
        raise ValueError("Os dados de entrada devem ser um array NumPy.")
    if dados.shape[1] != X_train.shape[1]:  # X_train.shape[1] é o número de colunas usadas no treino
        raise ValueError(f"Os dados devem ter {X_train.shape[1]} colunas.")
 
# Exemplo de uso no backend para normalizar novos dados antes da previsão
def prever(dados):
    dados_normalizados = scaler.transform(dados)  # Normalizar os dados
    resultado = modelo.predict(dados_normalizados)  # Realizar a previsão
    return resultado

def home(request):
    """
    Renderiza a página inicial do app 'clientes'.
    """
    return render(request, 'clientes/home.html')  # Certifique-se de que o template existe

def preprocessar_dados(dados_entrada, scaler, label_encoder, num_features=16):
    """
    Função para processar os dados de entrada de acordo com a necessidade do modelo.
    """
    # Convertendo os dados de entrada para DataFrame
    df = pd.DataFrame([dados_entrada])

    # Adicionando as colunas numéricas com valores padrão (zeros)
    num_colunas = num_features - df.shape[1]  # Quantidade de colunas numéricas necessárias
    for _ in range(num_colunas):
        df[f'num_feature_{_}'] = 0  # Adiciona colunas numéricas com valor 0

    # Reordenando as colunas para garantir que a ordem esteja de acordo com o modelo
    df = df[sorted(df.columns)]

    # Aplicando a codificação LabelEncoder às variáveis categóricas
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = df[column].apply(
            lambda x: label_encoder.transform([x])[0] if x in label_encoder.classes_ else -1
        )

    # Transformando os dados com o scaler usado no treinamento
    dados_entrada_processados = scaler.transform(df)

    return dados_entrada_processados


def consultar_credito(request):
    form = ConsultaCreditoForm()
    resultado = None

    if request.method == 'POST':
        form = ConsultaCreditoForm(request.POST)
        if form.is_valid():
            # Obter os dados do formulário
            cliente = form.save(commit=False)
            dados_entrada = {
                "sexo": cliente.sexo,
                "regiao": cliente.regiao,
                "estado_civil": cliente.estado_civil,
                "numero_filhos": cliente.numero_filhos,
                "propriedade": cliente.propriedade,
                "educacao": cliente.educacao,
                "vinculo_empregaticio": cliente.vinculo_empregaticio,
                "fonte_renda": cliente.fonte_renda,
            }
            
            cliente.previsao_resultado = resultado
            cliente.save() 
            try:
                # Processar os dados de entrada
                dados_entrada_processados = preprocessar_dados(dados_entrada, scaler, label_encoder)

                # Ajustar a forma dos dados para (1, 16)
                dados_entrada_processados = dados_entrada_processados.reshape((1, 16))

                # Fazer a previsão com o modelo de IA
                
                previsao = modelo.predict(dados_entrada_processados)

                # Interpretando a previsão
                resultado = "Aptidão para concessão de empréstimo: Concedido!" if previsao[0][0] > 0.5 else "Aptidão para concessão de empréstimo: Negado!"

            except Exception as e:
                resultado = f"Erro no processamento: {str(e)}"

    return render(request, 'clientes/consultar_credito.html', {'form': form, 'resultado': resultado})


# Carregar o modelo ao iniciar
MODEL_PATH = 'C:/Users/limmw/OneDrive/Área de Trabalho/back-ia/creditobancario/model/modelo_treinado_cd.h5'
model = keras.models.load_model(MODEL_PATH)

# Views com documentação Swagger
class ClienteListView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]  # Permissão sem autenticação
    authentication_classes = []  # Sem autenticação


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
    permission_classes = [AllowAny]  # Permissão sem autenticação
    authentication_classes = []  # Sem autenticação

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
    permission_classes = [AllowAny]  # Permissão sem autenticação
    authentication_classes = []  # Sem autenticação

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
    permission_classes = [AllowAny]  # Permissão sem autenticação
    authentication_classes = []  # Sem autenticação

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
    permission_classes = [AllowAny]  # Permissão sem autenticação
    authentication_classes = []  # Sem autenticação

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
    # Remover a autenticação, se não for necessária
    permission_classes = [AllowAny]
    authentication_classes = []

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