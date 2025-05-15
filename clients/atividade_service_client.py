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

    @staticmethod
    def get_atividade_para_professor(id_atividade, id_professor):
        """
        Retorna a atividade filtrada para um professor específico, ocultando 'respostas'
        se o professor não leciona a disciplina.
        """
        try:
            response = requests.get(
                f"{ATIVIDADE_API_URL}/{id_atividade}/professor/{id_professor}"
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return None
        

        
