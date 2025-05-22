import pandas as pd
from google.cloud import bigquery
from app.config import Config
from app.fetch_data import get_top_cryptos
from datetime import datetime

client = bigquery.Client(project=Config.GCP_PROJECT_ID)

def ingest_data():
    assets = get_top_cryptos()
    now = datetime.utcnow()

    # ------------------ TABELA: cryptocurrencies ------------------
    df_crypto = pd.DataFrame([{
        "id": a["id"],
        "rank": int(a["rank"]),
        "name": a["name"],
        "symbol": a["symbol"],
        "supply": float(a["supply"]),
        "maxSupply": float(a["maxSupply"]) if a["maxSupply"] else None,
        "marketCapUsd": float(a["marketCapUsd"]),
        "volumeUsd24Hr": float(a["volumeUsd24Hr"]),
        "priceUsd": float(a["priceUsd"]),
        "changePercent24Hr": float(a["changePercent24Hr"]),
        "vwap24Hr": float(a["vwap24Hr"]) if a["vwap24Hr"] else None,
        "updatedAt": now
    } for a in assets])

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(df_crypto, Config.TABLE_CRYPTO, job_config=job_config)
    job.result()
    print("Tabela 'cryptocurrencies' carregada com sucesso!")

    # ------------------ TABELA: price_history ------------------
    df_history = pd.DataFrame([{
        "id": a["id"],
        "priceUsd": float(a["priceUsd"]),
        "volumeUsd24Hr": float(a["volumeUsd24Hr"]),
        "marketCapUsd": float(a["marketCapUsd"]),
        "recordedAt": now
    } for a in assets])

    job_config_hist = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    job_hist = client.load_table_from_dataframe(df_history, Config.TABLE_HISTORY, job_config=job_config_hist)
    job_hist.result()
    print("Tabela 'price_history' carregada com sucesso!")
