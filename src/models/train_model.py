from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import mlflow
import mlflow.sklearn

class Train:

    def train_knn(self, x_train, x_test, y_train, y_test, n_neighbors):
        """
        Trains a K-Nearest Neighbors (KNN) model and logs the experiment in MLflow.

        Parameters:
        x_train (array-like): Training data.
        x_test (array-like): Test data.
        y_train (array-like): Training labels.
        y_test (array-like): Test labels.
        n_neighbors (int): Number of neighbors to use in the KNN algorithm.
        """
        
        # MLflow experiment name
        experiment_name = "mlflow-experiment-diabetes"
        # mlflow.set_experiment(experiment_name)  # Set the experiment in MLflow
        
        # Start a new run of the experiment in MLflow
        with mlflow.start_run():
            
            # Automatically log parameters, metrics, and models
            mlflow.sklearn.autolog()
            
            # Initialize the KNN model with the specified parameters
            knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric='minkowski', p=2)
            
            # Train the model
            knn.fit(x_train, y_train)
            
            # Make predictions on the test set
            Y_pred_knn = knn.predict(x_test)
            
            # Calculate the accuracy of the model
            score_knn = round(accuracy_score(y_test, Y_pred_knn) * 100, 2)
            print(f"KNN model accuracy: {score_knn}%")
            
            # Log the trained model in MLflow
            mlflow.sklearn.log_model(knn, "diabetesPredict")
