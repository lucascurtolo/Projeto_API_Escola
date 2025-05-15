import requests

ATIVIDADE_API_URL = "http://localhost:5002/atividades"

class AtividadeServiceClient:
    @staticmethod
    def get_atividades():
        try:
            response = requests.get(ATIVIDADE_API_URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return []

    @staticmethod
    def get_atividade(id_atividade):
        try:
            response = requests.get(f"{ATIVIDADE_API_URL}/{id_atividade}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return None
