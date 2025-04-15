import os
import yaml
import subprocess

CONFIG_PATH = "config_server.yaml"

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config(CONFIG_PATH)
    folder_name = config.get("store_folder_name", "mlruns_default")
    storage_dir = f"..\store\{folder_name}"

    # Cria o diretório se não existir
    os.makedirs(storage_dir, exist_ok=True)

    # Comando do MLflow
    command = [
        "mlflow", "server",
        "--backend-store-uri", storage_dir,
        "--default-artifact-root", storage_dir,
        "--host", "127.0.0.1",
        "--port", "5000"
    ]

    print(f"Iniciando MLflow com store: {storage_dir}")
    subprocess.run(command)

if __name__ == "__main__":
    main()
