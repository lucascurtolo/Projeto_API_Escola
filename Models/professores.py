from Models.models import Professores
from Config import db

class Professores_Repository:
    def __init__(self):
        pass
    
    def criar_professor(self, id, nome, disciplina):
        try:
            id_existente = Professores.query.filter_by(id=id).first()
            if id_existente:
                raise ValueError("Professor com este id já existe")
            
            novo_professor = Professores(id = id, nome = nome, disciplina= disciplina)
            db.session.add(novo_professor)
            db.session.commit()
            return novo_professor
        except ValueError as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar professor: {str(e)}")

    def listar_professor(self, id):
        professor = Professores.query.filter_by(id=id).first()
        if not professor:
            raise ValueError("Professor não encontrado")
        return professor
            
    

    def listar_todos_professores(self):
        return Professores.query.all()


    def atualizar_professores(self, id, nome=None, disciplina=None):
        professor = Professores.query.filter_by(id=id).first()
        if not professor:
            raise ValueError("Professor não encontrado.")
        if nome:
            professor.nome = nome
        if disciplina:
            professor.disciplina = disciplina
        db.session.commit()
        return professor



    def excluir_professores(self, id):
        try:
            professor = Professores.query.filter_by(id =id).first()
            if professor:
                db.session.delete(professor)
                db.session.commit()
            return professor
        except:
            db.session.rollback()
            raise ValueError("Erro ao excluir professor")

    
    def excluir_todos_professores(self):
        try:
            professores = Professores.query.all()
            if not professores:
                raise ValueError("Não há professores para excluir")
            
            for professor in professores:
                db.session.delete(professor)
            db.session.commit()
            return {"message": "Todos os professores foram excluídos"}
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao excluir professores: {str(e)}")
    
    
class NoData(Exception):
    pass
            
