import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key_google.json"

from app.ingest import ingest_data

def main():
    print("Iniciando ingestão de dados de criptomoedas...")
    ingest_data()
    print("Processo finalizado com sucesso.")

if __name__ == "__main__":
    main()
