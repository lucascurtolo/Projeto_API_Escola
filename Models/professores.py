from Models.models import Professores

class ProfessoresRepository:
    def __init__(self):
        self.professores = {}
    
    def criar_professor(self, professor):
        if professor.id in self.professores:
            raise ValueError("professores com este ID já existe.")
        self.professores[professor.id] = professor
        return professor

    def listar_professor(self, id):
        try:
            return self.professores[id]
        except:
            raise ValueError("professores não encontrado")
    

    def listar_todos_professores(self):
        return list (self.professores.values())


    def atualizar_professores(self, id, nome=None, disciplina=None):
        professores = self.professores.get(id)
        if not professores:
            raise ValueError("professores não encontrado.")
        if nome:
            professores.nome = nome
        if disciplina:
            professores.idade = disciplina 
        return professores


    def excluir_professores(self, id):
        if id not in self.professores:
            raise ValueError("Professor não encontrado.")
        return self.professores.pop(id)

    

    def excluir_todos_professores(self):
        qtd_professores = len(self.professores)
        if qtd_professores == 0:
            raise ValueError("Não há professores para excluir")
    
        self.professores.clear()
        return {"mensagem": "Todos os professores foram excluídos."}
