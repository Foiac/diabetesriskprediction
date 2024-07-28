from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import mlflow
import mlflow.sklearn

def train_knn(x_train, x_test, y_train, y_test, n_neighbors):
    """
    Treina um modelo K-Nearest Neighbors (KNN) e registra o experimento no MLflow.

    Parâmetros:
    x_train (array-like): Dados de treino.
    x_test (array-like): Dados de teste.
    y_train (array-like): Rótulos de treino.
    y_test (array-like): Rótulos de teste.
    n_neighbors (int): Número de vizinhos a serem usados no algoritmo KNN.
    """
    
    # Nome do experimento MLflow
    experiment_name = "mlflow-experiment-diabetes"
    mlflow.set_experiment(experiment_name)  # Define o experimento no MLflow
    
    # Inicia uma nova execução de experimento no MLflow
    with mlflow.start_run():
        
        # Registra automaticamente os parâmetros, métricas e modelos
        mlflow.sklearn.autolog()
        
        # Inicializa o modelo KNN com os parâmetros especificados
        knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric='minkowski', p=2)
        
        # Treina o modelo
        knn.fit(x_train, y_train)
        
        # Faz previsões no conjunto de teste
        Y_pred_knn = knn.predict(x_test)
        
        # Calcula a acurácia do modelo
        score_knn = round(accuracy_score(y_test, Y_pred_knn) * 100, 2)
        print(f"Acurácia do modelo KNN: {score_knn}%")
        
        # Registra o modelo treinado no MLflow
        mlflow.sklearn.log_model(knn, "diabetesPredict")