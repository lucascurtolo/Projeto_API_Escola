import requests

PESSOA_API_URL = "http://localhost:5001/pessoas"

class PessoaServiceClient:
    @staticmethod
    def get_professores():
        try:
            response = requests.get(f"{PESSOA_API_URL}/professores")
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return []

    @staticmethod
    def get_alunos():
        try:
            response = requests.get(f"{PESSOA_API_URL}/alunos")
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return []

    @staticmethod
    def verificar_leciona(id_professor, id_disciplina):
        try:
            response = requests.get(f"{PESSOA_API_URL}/leciona/{id_professor}/{id_disciplina}")
            response.raise_for_status()
            return response.json().get("leciona", False)
        except requests.RequestException:
            return False
