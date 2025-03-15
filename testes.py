import unittest
from main import app 

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

        self.assertEqual(type(objeto_retornado), list) 

if __name__ == "__main__":
    unittest.main() 
