import requests
from app.config import Config

def get_top_cryptos(limit=100):
    url = "https://rest.coincap.io/v3/assets"
    headers = {"Authorization": f"Bearer {Config.COINCAP_API_KEY}"}
    params = {"limit": limit}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["data"]
