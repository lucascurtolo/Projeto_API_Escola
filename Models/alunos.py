from Models.models import Alunos
from Config import db
  

class AlunosModel:
    def __init__(self):
        pass

    def criar_aluno(self, nome, idade, turma_id=None):
        try:
            aluno_existente = Alunos.query.filter_by(nome=nome).first()
            if aluno_existente:
                raise ValueError("Aluno com este nome já existe.")

            novo_aluno = Alunos(nome=nome, idade=idade, turma_id=turma_id)
            db.session.add(novo_aluno)
            db.session.commit()
            return novo_aluno

        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar aluno: {str(e)}")

    def listar_aluno(self, id):
        try:
            aluno = Alunos.query.filter_by(id=id).one()  
            return aluno
        except ValueError:
            raise ValueError("Aluno não encontrado")

    def listar_todos_alunos(self):
        return Alunos.query.all()

    def atualizar_aluno(self, id, nome=None, idade=None, turma_id = None):
        aluno = Alunos.query.filter_by(id=id).first()

        if aluno:
            if nome:
                aluno.nome = nome
            if idade:
                aluno.idade = idade
            if turma_id:
                aluno.turma_id = turma_id

            db.session.commit()
            return aluno
        else:
            raise ValueError("Aluno não encontrado.")

    def excluir_aluno(self, id):
        aluno = Alunos.query.filter_by(id=id).first()

        if aluno:
            db.session.delete(aluno)
            db.session.commit()
            return aluno
        else:
            raise ValueError("Aluno não encontrado")

    def excluir_todos_alunos(self):
        alunos = Alunos.query.all()
        if not alunos:
            raise ValueError("Não há alunos para excluir")

        for aluno in alunos:
            db.session.delete(aluno)

        db.session.commit()
        return {"mensagem": "Todos os alunos foram excluídos."}


class NoData(Exception):
    pass
