import requests

def fetch_campaign_data(api_url: str, campaign_id: str) -> dict:
    # Busca informações de uma campanha de um serviço externo
    response = requests.get(f"{api_url}/campaigns/{campaign_id}")
    if response.status_code == 200:
        return response.json()
    raise ValueError(f"Erro ao buscar campanha: {response.status_code}")
