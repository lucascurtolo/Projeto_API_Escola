from Models.models import Alunos  # Importando a classe Alunos
from Config import db
from datetime import datetime

class Alunos_Repository:
    def __init__(self):
        pass

    def criar_aluno(self, id, nome, data_nascimento_str, nota_primeiro_semestre, nota_segundo_semestre, turma_id=None):
        try:
            # Verifica se já existe um aluno com esse ID
            aluno_existente = Alunos.query.filter_by(id=id).first()
            if aluno_existente:
                raise ValueError("Aluno com este id já existe.")
            
            # Verifica se a data de nascimento é uma string
            if not isinstance(data_nascimento_str, str):
                raise ValueError("Data de nascimento deve ser uma string.")
            
            # Converte a data de nascimento para datetime.date
            data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
            
            # Calcula a idade do aluno
            idade = Alunos.calcular_idade(data_nascimento)
            
            # Calcula a média final
            media_final = (nota_primeiro_semestre + nota_segundo_semestre) / 2

            # Cria o novo aluno
            novo_aluno = Alunos(
                id=id,  
                nome=nome,
                idade=idade,
                turma_id=turma_id,
                data_nascimento=data_nascimento,
                nota_primeiro_semestre=nota_primeiro_semestre,
                nota_segundo_semestre=nota_segundo_semestre,
                media_final=media_final
            )

            # Adiciona o novo aluno ao banco de dados
            db.session.add(novo_aluno)
            db.session.commit()
            return novo_aluno

        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar aluno: {str(e)}")


    def listar_aluno(self, id):
        try:
            aluno = Alunos.query.filter_by(id=id).first()  
            return aluno
        except ValueError:
            raise ValueError("Aluno não encontrado")

    def listar_todos_alunos(self):
        return Alunos.query.all()

    def atualizar_aluno(self, id, nome=None, idade=None, turma_id=None, data_nascimento=None,
                        nota_primeiro_semestre=None, nota_segundo_semestre=None, media_final=None):
        aluno = Alunos.query.filter_by(id=id).first()

        if aluno:
            if nome is not None:
                aluno.nome = nome
            if idade is not None:
                aluno.idade = idade
            if turma_id is not None:
                aluno.turma_id = turma_id
            if data_nascimento is not None:
                aluno.data_nascimento = data_nascimento
            if nota_primeiro_semestre is not None:
                aluno.nota_primeiro_semestre = nota_primeiro_semestre
            if nota_segundo_semestre is not None:
                aluno.nota_segundo_semestre = nota_segundo_semestre
            if media_final is not None:
                aluno.media_final = media_final

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
