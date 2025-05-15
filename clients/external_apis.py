import requests

PESSOA_API_URL = "http://localhost:5001/pessoas"
ATIVIDADE_API_URL = "http://localhost:5002/atividades"

def get_pessoas():
    try:
        response = requests.get(f"{PESSOA_API_URL}/professores")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return []
    

def get_atividades():
    try:
        response = requests.get(f"{ATIVIDADE_API_URL}/atividades")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return []


    