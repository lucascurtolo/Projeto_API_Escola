import unittest
from main import app 
from main import alunos_db, professores_db

class Testes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True  
        self.client = app.test_client() 

    def test_0_alunos_retorna_lista(self):
        response = self.client.get('/alunos_list')
        self.assertEqual(response.status_code, 200)

        try:
            objeto_retornado = response.get_json()
        except ValueError:
            self.fail("Foi retornado outra coisa e não um JSON.")

        
        self.assertEqual(type(objeto_retornado["alunos"]), list)


    def test_01_cria_aluno(self):
        aluno_data = {
            "id": 10,
            "nome": "Omena",
            "idade": 19
        }
        response = self.client.post('/alunos', json=aluno_data)
        self.assertEqual(response.status_code, 201)

        resposta_json = response.get_json()
        self.assertEqual(resposta_json["id"], aluno_data["id"])
        self.assertEqual(resposta_json["nome"], aluno_data["nome"])
        self.assertEqual(resposta_json["idade"], aluno_data["idade"])

        self.assertIsNotNone(aluno_data)
        self.assertEqual(aluno_data["nome"], aluno_data["nome"])
        self.assertEqual(aluno_data["idade"], aluno_data["idade"])
    
    def test_02_listar_aluno_por_id(self):
        response = self.client.get("/alunos/5")
        self.assertEqual(response.status_code, 200)

        alunos_data = response.get_json()

        self.assertEqual(alunos_data['id'], 5)
        self.assertEqual(alunos_data["nome"], "Marcelo" )

        
    def test_03_listar_aluno_sem_id(self):
        response = self.client.get("/alunos/999")
        self.assertEqual(response.status_code, 404)

        erro_data = response.get_json()

        self.assertEqual(erro_data["erro"], "Aluno não encontrado")

    def test_04_apagar_lista_aluno(self):
        response = self.client.delete("/alunos_list")
        self.assertEqual(response.status_code, 204)  

        
        self.assertEqual(response.get_data(), b'')

    def test_05_listar_professor_sem_id(self):
        response = self.client.get("/professores/999")
        self.assertEqual(response.status_code, 404)

        erro_data = response.get_json()

        self.assertEqual(erro_data["message"], "Professor não encontrado")


    def test_06_apagar_lista_professor(self):
        response = self.client.delete("/professores_list")
        self.assertEqual(response.status_code, 204)

        self.assertEqual(response.get_data(), b'')

    def test_07_deletar_aluno_por_id(self):
        for aluno in alunos_db:
            if aluno.id == id:
                return None
        self.assertIsNotNone(alunos_db, "Aluno com ID 5 não encontrado antes da exclusão")
        response = self.client.delete("/alunos/5")
        self.assertEqual(response.status_code, 204)

        self.assertEqual(response.get_data(), b"")

        aluno_removido = next((aluno for aluno in alunos_db if aluno.id == 5), None)
        self.assertIsNone(aluno_removido, "Aluno com ID 5 não foi removido da lista após a exclusão")
    
    def test_08_deletar_professor_por_id(self):
        for professor in professores_db:
            if professor.id == id:
                return None
        self.assertIsNotNone(professores_db, "professor com ID 5 não encontrado antes da exclusão")
        response = self.client.delete("/professores/5")
        self.assertEqual(response.status_code, 204)

        self.assertEqual(response.get_data(), b"")

        professor_removido = next((professor for professor in professores_db if professor.id == 5), None)
        self.assertIsNone(professor_removido, "professor com ID 5 não foi removido da lista após a exclusão")

    def test_09_cria_professor(self):
        professor_data = {
            "id": 6,
            "nome": "Julio",
            "disciplina": "Linguagem de programação"
        }
        response = self.client.post('/professores', json=professor_data)
        self.assertEqual(response.status_code, 201)

        resposta_json = response.get_json()
        self.assertEqual(resposta_json["id"], professor_data["id"])
        self.assertEqual(resposta_json["nome"], professor_data["nome"])
        self.assertEqual(resposta_json["disciplina"], professor_data["disciplina"])

        self.assertIsNotNone(professor_data)
        self.assertEqual(professor_data["nome"], professor_data["nome"])
        self.assertEqual(professor_data["disciplina"], professor_data["disciplina"])
    










  




if __name__ == "__main__":
    unittest.main() 
