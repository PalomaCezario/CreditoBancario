import tensorflow as tf

# Função para carregar o modelo
def load_trained_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
        print("Modelo carregado com sucesso!")
        return model
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None
