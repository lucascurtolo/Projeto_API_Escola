from Models.models import Turmas

class TurmasModel:
    def __init__(self):
        self.turmas = {}

    def criar_turma(self, turma):
        if turma.id in self.turmas:
            raise ValueError("Turma com este ID já existe.")
        self.turmas[turma.id] = turma
        return self.turmas

    def listar_turma(self, id):
        try:
            return self.turmas[id]
        except KeyError:
            raise ValueError("Turma não encontrada.")

    def listar_todas_turmas(self):
        return list(self.turmas.values())

    def atualizar_turma(self, id, nome=None, professor_id=None):
        turma = self.turmas.get(id)
        if not turma:
            raise ValueError("Turma não encontrada.")
        if nome:
            turma.nome = nome
        if professor_id:
            turma.professor_id = professor_id  
        return turma

    def excluir_turma(self, id):
        turma = self.turmas.pop(id, None)
        if not turma:
            raise ValueError("Turma não encontrada para excluir.")

    def excluir_todas_turmas(self):
        self.turmas.clear()
        return {"mensagem": "Todas as turmas foram excluídas."}