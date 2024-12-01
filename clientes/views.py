from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ClienteSerializer
from .models import Cliente
import numpy as np
import keras

# Carregar o modelo ao iniciar
MODEL_PATH = 'C:/Users/limmw/OneDrive/Área de Trabalho/back-ia - Copia/creditobancario/model/modelo_treinado_cd.h5'
model = keras.models.load_model(MODEL_PATH)

# Cliente Views
class ClienteListView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ClienteDetailView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ClienteUpdateView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ClienteDeleteView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

# Predict View
class PredictView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        try:
            # Verifica se o modelo foi carregado
            if model is None:
                return Response({'error': 'Modelo não carregado corretamente.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Lê os dados enviados pelo cliente
            data = request.data
            if not data or 'inputs' not in data:
                return Response({'error': 'Dados inválidos ou ausentes.'}, status=status.HTTP_400_BAD_REQUEST)

            # Verifica se o número de características está correto (16)
            input_data = np.array(data['inputs'])
            if input_data.shape[0] != 16:
                return Response({'error': f"Número incorreto de características. Esperado 16, mas recebido {input_data.shape[0]}."}, status=status.HTTP_400_BAD_REQUEST)

            # Converte os dados para o formato correto (uma amostra)
            input_data = input_data.reshape(1, -1)

            # Realiza a predição
            predictions = model.predict(input_data)

            # Retorna a resposta
            response = {'prediction': predictions.tolist()}
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            # Retorna erro com a mensagem
            return Response({'error': f"Erro ao processar: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
