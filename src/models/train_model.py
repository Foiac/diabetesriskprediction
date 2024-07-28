from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import mlflow
import mlflow.sklearn

def train_knn(x_train, x_test, y_train, y_test, n_neighbors):

    experiment_name = "mlflow-experiment-diabetes"
    mlflow.set_experiment(experiment_name)
    n_neighbors = n_neighbors #24
    
    with mlflow.start_run():
        
        mlflow.sklearn.autolog()

        knn = KNeighborsClassifier(n_neighbors = n_neighbors, metric = 'minkowski', p = 2)
        knn.fit(x_train, y_train)

        Y_pred_knn=knn.predict(x_test)
        score_knn = round(accuracy_score(y_test, Y_pred_knn)*100, 2)

        mlflow.sklearn.log_model(knn, "diabetesPredict")