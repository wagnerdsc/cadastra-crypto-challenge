# 📊 Desafio Técnico - Coleta de Criptomoedas

O objetivo deste projeto é desenvolver uma solução completa e escalável para **monitoramento das 100 principais criptomoedas em D-1**, unindo:

- **Coleta automatizada de dados** da API CoinCap Pro;
- **Armazenamento estruturado** no Google BigQuery;
- **Visualização interativa** via Looker Studio.

A arquitetura da solução está dividida em duas camadas principais de dados:

- **`cryptocurrencies`**: visão atualizada das principais métricas do mercado, como preço, volume 24h e capitalização.
- **`price_history`**: registro histórico dos dados ao longo do tempo para análise de tendências e variações de mercado.

## 🧱 Tecnologias
- Python 3.11
- Google BigQuery (Free Tier)
- Looker Studio
- CoinCap Pro API

## 📁 Estrutura
- `app/`: scripts modulares
- `main.py`: executa o pipeline

## 🔐 Arquivos de configuração de ambiente
Certifique-se de configurar as variaveis de ambiente nesse arquivo:
- `.env`
- `key_google.json`

## 🔐 Exemplo de `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
COINCAP_API_KEY=
GCP_PROJECT_ID=seu-projeto-id
BQ_DATASET=seu_dataset
```

## 📁 Estrutura das tabelas no BQ

```sql
Tabela: cryptocurrencies
CREATE TABLE `seu-projeto.seu_dataset.cryptocurrencies` (
  id STRING,
  rank INT64,
  name STRING,
  symbol STRING,
  supply FLOAT64,
  maxSupply FLOAT64,
  marketCapUsd FLOAT64,
  volumeUsd24Hr FLOAT64,
  priceUsd FLOAT64,
  changePercent24Hr FLOAT64,
  vwap24Hr FLOAT64,
  updatedAt DATETIME
);

Tabela: price_history
CREATE TABLE `seu-projeto.seu_dataset.price_history` (
  id STRING,
  priceUsd FLOAT64,
  volumeUsd24Hr FLOAT64,
  marketCapUsd FLOAT64,
  recordedAt TIMESTAMP
);
```

## 📊 Dashboard
🔗 [Acessar no Looker Studio](https://lookerstudio.google.com/reporting/cd4e1f06-bf0e-4028-a089-5f4a25c05a87)

## 🚀 Execução

```bash
pip install -r requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS="key_google.json"
python main.py
