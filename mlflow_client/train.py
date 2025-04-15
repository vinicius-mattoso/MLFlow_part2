import mlflow
import mlflow.sklearn
import yaml
from datetime import datetime
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def main():
    # 1. Carrega configurações
    config = load_config()
    tracking_uri = config.get("tracking_uri", "http://127.0.0.1:5000")
    experiment_name = config["experiment"]["name"]
    run_base_name = config["experiment"]["run_name"]

    # 2. Gera timestamp e run name único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_name = f"{run_base_name}_{timestamp}"

    # 3. Conecta ao servidor MLflow
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

    # 4. Inicia o run
    with mlflow.start_run(run_name=run_name):
        # Dataset
        data = load_wine()
        X_train, X_test, y_train, y_test = train_test_split(
            data.data, data.target, test_size=0.2, random_state=42
        )

        # Modelo
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Avaliação
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        # Log de params e métricas
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

        print(f"Run '{run_name}' finalizado com acurácia: {acc:.4f}")


if __name__ == "__main__":
    main()
