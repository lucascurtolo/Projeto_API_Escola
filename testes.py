import unittest
from Config import create_app, db
from datetime import date
from Models.models import Alunos


class Testes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()  
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
        
    def tearDown(self):
        """Limpa o banco de dados após cada teste"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all() 

    def test_0_alunos_retorna_lista(self):
        response = self.client.get('/alunos')
        self.assertEqual(response.status_code, 200)

        try:
            objeto_retornado = response.get_json()
        except ValueError:
            self.fail("Foi retornado outra coisa e não um JSON.")


    def test_01_cria_aluno(self):
        aluno_data = {
            "id": 10,
            "nome": "Omena",
            "turma_id": 5,
            "data_nascimento": "2005-03-15",  # Data de nascimento
            "nota_primeiro_semestre": 6,
            "nota_segundo_semestre": 6,
            "media_final": 6  # A média final é calculada automaticamente também
        }

      
        response = self.client.post('/alunos/', json=aluno_data)
        self.assertEqual(response.status_code, 201)

        resposta_json = response.get_json()

        self.assertEqual(resposta_json["id"], aluno_data["id"])
        self.assertEqual(resposta_json["nome"], aluno_data["nome"])

        idade_calculada = Alunos.calcular_idade(date(2005, 3, 15))
        self.assertEqual(resposta_json["idade"], idade_calculada)

        media_calculada = (aluno_data["nota_primeiro_semestre"] + aluno_data["nota_segundo_semestre"]) / 2
        self.assertEqual(resposta_json["media_final"], media_calculada)

        self.assertIsNotNone(resposta_json)
        self.assertEqual(resposta_json["nome"], aluno_data["nome"])
        self.assertEqual(resposta_json["media_final"], media_calculada)


    
    def test_02_listar_aluno_por_id(self):
        aluno_data = {
            "id": 5,
            "nome": "Marcelo",
            "idade": 25,
            "turma_id": 4,
            "data_nascimento": "2004-05-05",
            "nota_primeiro_semestre": 8,
            "nota_segundo_semestre": 5,
            "media_final": 6

        }
        self.client.post("/alunos/", json=aluno_data)

        response = self.client.get("/alunos/5")
        self.assertEqual(response.status_code, 200)

        alunos_data = response.get_json()
        self.assertEqual(alunos_data['id'], 5)
        self.assertEqual(alunos_data["nome"], "Marcelo")

        
    def test_03_listar_aluno_sem_id(self):
        response = self.client.get("/alunos/999")
        self.assertEqual(response.status_code, 404)

        erro_data = response.get_json()

        self.assertEqual(erro_data["message"], "Aluno não encontrado")

    def test_04_apagar_lista_aluno(self):
        self.client.post("/alunos/", json = {
            "id": 555,
            "nome": "Teste",
            "idade": 15,
            "turma_id": 10,
            "data_nascimento": "2003-03-18",
            "nota_primeiro_semestre": 10,
            "nota_segundo_semestre": 10,
            "media_final": 10
        })
        response = self.client.delete("/alunos/")
        self.assertEqual(response.status_code, 204)


    def test_05_listar_professor_sem_id(self):
        response = self.client.get("/professores/999")
        self.assertEqual(response.status_code, 404)

        erro_data = response.get_json()

        self.assertEqual(erro_data["message"], "Professor não encontrado")

    def test_06_apagar_lista_professor(self):
        self.client.post("/professores", json={
            "nome": "Carlos",
            "idade": 50
        })

        response = self.client.delete("/professores")
        self.assertIn(response.status_code, [204, 404])

        if response.status_code == 204:
            self.assertEqual(response.get_data(), b'')

        elif response.status_code == 404:
            data = response.get_json()
            self.assertIn("message", data)
            self.assertEqual(data["message"], "Erro ao excluir professores")


    def test_07_deletar_aluno_por_id(self):
    
        novo_aluno = {
            "id": 999,  
            "nome": "Aluno Teste",
            "idade": 18,
            "turma_id": 1,
            "data_nascimento": "2002-06-25",
            "nota_primeiro_semestre": 5,
            "nota_segundo_semestre": 5,
            "media_final": 5
        }
        response = self.client.post("/alunos/", json=novo_aluno)
        self.assertEqual(response.status_code, 201)

        id_aluno = novo_aluno["id"]

        response = self.client.get(f"/alunos/{id_aluno}")
        self.assertEqual(response.status_code, 200)

        response = self.client.delete(f"/alunos/{id_aluno}")
        self.assertEqual(response.status_code, 204)

        response = self.client.get(f"/alunos/{id_aluno}")
        self.assertEqual(response.status_code, 404)


    def test_08_deletar_professor_por_id(self):

        novo_professor = {
            "id": 999,
            "nome": "Professor Teste",
            "disciplina": "Português",
            "idade": 45
        }
        response = self.client.post("/professores/", json=novo_professor)
        self.assertEqual(response.status_code, 201)

        response = self.client.delete("/professores/999")
        self.assertEqual(response.status_code, 204)

        response = self.client.get("/professores/999")
        self.assertEqual(response.status_code, 404)


    def test_09_cria_professor(self):
        professor_data = {
            "id": 5,
            "nome": "Julio",
            "disciplina": "Linguagem de programação",
            "idade": 48
        }
        response = self.client.post('/professores/', json=professor_data)
        self.assertEqual(response.status_code, 201)

        resposta_json = response.get_json()
        self.assertEqual(resposta_json["id"], professor_data["id"])
        self.assertEqual(resposta_json["nome"], professor_data["nome"])
        self.assertEqual(resposta_json["disciplina"], professor_data["disciplina"])
        self.assertEqual(resposta_json["idade"], professor_data["idade"])

        self.assertIsNotNone(professor_data)
        self.assertEqual(professor_data["nome"], professor_data["nome"])
        self.assertEqual(professor_data["disciplina"], professor_data["disciplina"])

    
    def test_10_professor_retorna_lista(self):
        response = self.client.get('/professores/')
        self.assertEqual(response.status_code, 200)

        try:
            objeto_retornado = response.get_json()
        except ValueError:
            self.fail("Foi retornado outra coisa e não um JSON.")

        
        self.assertEqual(type(objeto_retornado), list)
    

    def teste_11_criar_turma(self):
        turma_data = {
            "id": 5,
            "nome": "3A",
            "professor_id": 6
        }


        response = self.client.post('/turmas/', json=turma_data)
        self.assertEqual(response.status_code, 201)

        resposta_json = response.get_json()
        self.assertEqual(resposta_json["id"], turma_data["id"])
        self.assertEqual(resposta_json["nome"], turma_data["nome"])
        self.assertEqual(resposta_json["professor_id"], turma_data["professor_id"])

        self.assertIsNotNone(turma_data)
        self.assertEqual(turma_data["nome"], turma_data["nome"])
        self.assertEqual(turma_data["professor_id"], turma_data["professor_id"])
    
    def test_12_listar_turma_sem_id(self):
        response = self.client.get("/turmas/999")
        self.assertEqual(response.status_code, 404)

        erro_data = response.get_json()

        self.assertEqual(erro_data["erro"], "Turma não encontrada")
    
    def test_13_apagar_lista_turma(self):
        self.client.post("/turmas/", json = {
            "id": 154,
            "nome": "Turma Teste",
            "professor_id": 154
        })
        response = self.client.delete("/turmas/")
        self.assertEqual(response.status_code, 204)
    
    def test_14_turmas_retorna_lista(self):
        response = self.client.get('/turmas/')
        self.assertEqual(response.status_code, 200)

        try:
            objeto_retornado = response.get_json()
        except ValueError:
            self.fail("Foi retornado outra coisa e não um JSON.")

        
        self.assertEqual(type(objeto_retornado), list)

    def test_15_editar_nome_do_aluno(self):
        # Cria o aluno com todos os dados
        response = self.client.post('/alunos/', json={
            'id': 30,
            'nome': 'Cadu Mendes',
            'idade': 40,
            'turma_id': 6,
            'data_nascimento': '1985-03-26',
            'nota_primeiro_semestre': 6,
            'nota_segundo_semestre': 6,
            'media_final': 6
        })
        self.assertEqual(response.status_code, 201)

        # Busca o aluno antes da edição
        r_antes = self.client.get('/alunos/30')
        dados_antes = r_antes.json
        self.assertEqual(dados_antes['nome'], "Cadu Mendes")

        # Atualiza apenas o nome, mantendo os outros dados
        dados_antes['nome'] = "Carlos Eduardo Mendes"
        response = self.client.put("/alunos/30", json=dados_antes)
        self.assertEqual(response.status_code, 200)

        # Busca o aluno depois da edição
        r_depois = self.client.get("/alunos/30")
        dados_depois = r_depois.json
        self.assertEqual(dados_depois["id"], 30)
        self.assertEqual(dados_depois["nome"], "Carlos Eduardo Mendes")
        self.assertEqual(dados_depois["idade"], 40)

    def test_16_editar_nome_professor(self):
        response = self.client.post('/professores/', json={'nome': 'Andreia', 'id': 15, 'disciplina': "Soft Skill", 'idade': 40})
        
        self.assertEqual(response.status_code, 201)

        r_antes = self.client.get('/professores/15')
        
        self.assertEqual(r_antes.status_code, 200)
        
        dados_antes = r_antes.json

        self.assertIn('nome', dados_antes) 
        self.assertEqual(dados_antes['nome'], "Andreia")

        response = self.client.put("/professores/15", json={"nome": "Andreia Alterado"})
        self.assertEqual(response.status_code, 200)

        r_depois = self.client.get("/professores/15")
        dados_depois = r_depois.json
        self.assertEqual(dados_depois["id"], 15)
        self.assertEqual(dados_depois["nome"], "Andreia Alterado")
        self.assertEqual(dados_depois["disciplina"], "Soft Skill")
        self.assertEqual(dados_depois["idade"], 40)


    def test_17_editar_nome_turma(self):
        response = self.client.post('/turmas/', json = {'nome': '3C', 'id': 10, 'professor_id': 15 })
        self.assertEqual(response.status_code, 201)

        r_antes = self.client.get('/turmas/10')
        dados_antes = r_antes.json
        self.assertEqual(dados_antes["nome"], "3C")
        
        response = self.client.put("/turmas/10", json={"nome":"3D"})
        self.assertEqual(response.status_code, 200)

        r_depois = self.client.get("/turmas/10")
        dados_depois = r_depois.json
        self.assertEqual(dados_depois["id"], 10)
        self.assertEqual(dados_depois["nome"], "3D")
        


    
    


     
     
     
     
     

    










  




if __name__ == "__main__":
    unittest.main() 