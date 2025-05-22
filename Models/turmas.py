from Models.models import Turmas
from Config import db

class Turmas_Repository:
    def __init__(self):
        pass

    def criar_turma(self, id, nome, professor_id, id_disicplina):
        try:
            turma_existente = Turmas.query.filter_by(id = id).first()
            if turma_existente:
                raise ValueError("Turma já existe")
            nova_turma = Turmas(id = id, nome = nome, professor_id = professor_id, id_disciplina=id_disicplina)
            db.session.add(nova_turma)
            db.session.commit()
            return nova_turma
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar turma: {str(e)}" )
        

    def listar_turma(self, id):
        try:
            turma = Turmas.query.filter_by(id = id).first()
            return turma
        except:
            raise ValueError("Turma não encontrada")

    def listar_todas_turmas(self):
        return Turmas.query.all()

    def atualizar_turma(self, id, nome=None, professor_id=None, id_disciplina=None):
        turma = Turmas.query.filter_by(id=id).first() 
        if turma:
            if nome:
                turma.nome = nome  
            if professor_id:
                turma.professor_id = professor_id  
            if id_disciplina:
                turma.id_disciplina = id_disciplina
            db.session.commit() 
            return turma
        else:
            raise ValueError("Turma não encontrada")  


    def excluir_turma(self, id):
       turma = Turmas.query.filter_by(id = id).first()
       if turma:
           db.session.delete(turma)
           db.session.commit()
           return turma
       else:
           raise ValueError("Turma não encontrada")
           
        

    def excluir_todas_turmas(self):
        turmas = Turmas.query.all()
        if not turmas:
            raise ValueError("Não há turmas para excluir")
        for turma in turmas:
            db.session.delete(turma)
        db.session.commit()
        return{"message": "Todas as turmas foram excluídas."}

class NoData(Exception):
    pass
        

        