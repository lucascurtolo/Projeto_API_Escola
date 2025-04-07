from Models.models import Professores

class ProfessoresRepository:
    def __init__(self):
        self.professores = {}
    
    def criar_professores(self, professores):
        if professores.id in self.professoress:
            raise ValueError("professores com este ID já existe.")
        self.professoress[professores.id] = professores
        return professores

    def listar_professores(self, id):
        try:
            return self.professoress[id]
        except:
            raise ValueError("professores não encontrado")
    

    def listar_todos_professoress(self):
        return list (self.professoress.values())


    def atualizar_professores(self, id, nome=None, idade=None):
        professores = self.professoress.get(id)
        if not professores:
            raise ValueError("professores não encontrado.")
        if nome:
            professores.nome = nome
        if idade:
            professores.idade = idade 
        return professores


    def excluir_professores(self, id):
        professores = self.professoress.pop(id)
        if not professores:
            raise ValueError("Não há professoress para excluir")
        return professores
    

    def excluir_todos_professoress(self):
        qtd_professoress = len(self.professoress)
        if qtd_professoress == 0:
            raise ValueError("Não há professoress para excluir")
        
        self.professoress.clear()
        return  {"mensagem":"Todos os professoress foram excluídos."}