
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

class Config:
    # CoinCap
    COINCAP_API_KEY = os.getenv("COINCAP_API_KEY")

    # Google Cloud / BigQuery
    GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
    BQ_DATASET = os.getenv("BQ_DATASET")

    # Tabelas BigQuery (padrão)
    TABLE_CRYPTO = f"{GCP_PROJECT_ID}.{BQ_DATASET}.cryptocurrencies"
    TABLE_HISTORY = f"{GCP_PROJECT_ID}.{BQ_DATASET}.price_history"

    # Segurança
    @staticmethod
    def validate():
        required = [
            "COINCAP_API_KEY",
            "GCP_PROJECT_ID",
            "BQ_DATASET",
        ]
        for var in required:
            if not getattr(Config, var):
                raise EnvironmentError(f"Variável {var} não está definida no .env")

# Validações ao importar
Config.validate()
