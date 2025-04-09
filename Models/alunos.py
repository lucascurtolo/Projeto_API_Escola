from Models.models import Alunos
  

class AlunosModel:
    def __init__(self):
        self.alunos = {}

    def criar_aluno(self, aluno):
        if aluno.id in self.alunos:
            raise ValueError("Aluno com este ID já existe.")
        self.alunos[aluno.id] = aluno
        return aluno

    def listar_aluno(self, id):
        aluno = self.alunos.get(id)
        if not aluno:
            raise ValueError("Aluno não encontrado")
        return aluno

    def listar_todos_alunos(self):
        return list(self.alunos.values())

    def atualizar_aluno(self, id, nome=None, idade=None, turma_id = None):
        aluno = self.alunos.get(id)
        if not aluno:
            raise ValueError("Aluno não encontrado.")
        if nome:
            aluno.nome = nome
        if idade:
            aluno.idade = idade
        if turma_id: 
            aluno.turma_id = turma_id
        if id:
            aluno.id = id
        return aluno

    def excluir_aluno(self, id):
        aluno = self.alunos.pop(id, None)
        if not aluno:
            raise ValueError("Aluno não encontrado")
        return aluno

    def excluir_todos_alunos(self):
        if not self.alunos:
            raise ValueError("Não há alunos para excluir")
        self.alunos.clear()
        return {"mensagem": "Todos os alunos foram excluídos."}


class NoData(Exception):
    pass
