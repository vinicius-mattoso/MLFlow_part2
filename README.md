# # 🚀 MLFlow_PART2 — Projeto com MLflow Tracking Server Separado

Este projeto mostra como configurar um pipeline de experimentos com **MLflow** usando uma estrutura distribuída entre:

- Um **servidor MLflow Tracking** (em um terminal)
- Um **cliente de treinamento de modelos** (em outro terminal)

Com suporte a múltiplos modos de execução (Windows, Linux/macOS), e configuração flexível via YAML.

---

## 📁 Estrutura do Projeto
```bash
MLFlow_PART2/ 
│ 
├── README.md 
├── requirements.txt 
├── mlflow_server/ # Terminal 1 
│ └──config_server.yaml
│ └──run_server.bat # Windows
│ └──run_server.sh # Linux/macOS
│ └──start_server.py # Executável por Python (Windows ou Linux) 
│ 
└── store/ # Diretório com os dados do MLflow 
│  └──mlruns_<nome_definido> 
│ 
└── mlflow_client/ # Terminal 2
│  └──config.yaml  
│  └──train.py 
│  └──client_requirements.txt  
```

## ⚙️ 1. Instalação

### Ambiente para o servidor

```bash
cd MLFlow_PART2
pip install -r requirements.txt
```

### Ambiente para o cliente
```bash
cd MLFlow_PART2/mlflow_client
pip install -r client_requirements.txt
```
## 🚀 2. Executando o Projeto

🖥️ TERMINAL 1 — Subindo o servidor MLflow
Entre na pasta mlflow_server/ e escolha uma das opções abaixo:
```bash
cd mlflow_server
run_server.bat

or

cd mlflow_server
chmod +x run_server.sh
./run_server.sh

or

cd mlflow_server
python start_server.py
```

🖥️ TERMINAL 2 — Executando o cliente
```bash
cd mlflow_client
python train.py
```

### 📄 config.yaml
```bash
tracking_uri: "http://127.0.0.1:5000"

experiment:
  name: "wine_experiment"
  run_name: "baseline_model"
```

### 📊 Visualizando os Experimentos
```bash
http://127.0.0.1:5000
```

### 🧠 Funcionalidades principais

* 🌐 Separação entre cliente e servidor MLflow

* ⚙️ Configuração de tracking e nomes por YAML

* 📌 Logging de parâmetros, métricas e artefatos

* 💾 Armazenamento local de experimentos por projeto