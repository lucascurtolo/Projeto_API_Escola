from models import Alunos

class AlunosRepository:
    def __init__(self):
        self.alunos = {}
    
    def criar_aluno(self, aluno):
        if aluno.id in self.alunos:
            raise ValueError("Aluno com este ID já existe.")
        self.alunos[aluno.id] = aluno
        return aluno

    def listar_aluno(self, id):
        try:
            return self.alunos[id]
        except:
            raise ValueError("Aluno não encontrado")
    

    def listar_todos_alunos(self):
        return list (self.alunos.values())


    def atualizar_aluno(self, id, nome=None, idade=None):
        aluno = self.alunos.get(id)
        if not aluno:
            raise ValueError("Aluno não encontrado.")
        if nome:
            aluno.nome = nome
        if idade:
            aluno.idade = idade 
        return aluno


    def excluir_aluno(self, id):
        aluno = self.alunos.pop(id)
        if not aluno:
            raise ValueError("Não há alunos para excluir")
        return aluno
    

    def excluir_todos_alunos(self):
        qtd_alunos = len(self.alunos)
        if qtd_alunos == 0:
            raise ValueError("Não há alunos para excluir")
        
        self.alunos.clear()
        return  {"mensagem":"Todos os alunos foram excluídos."}
    