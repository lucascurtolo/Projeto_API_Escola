from config import db

class Professores(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    nome = db.Collumn(db.String(100))
    disciplina = db.Collumn(db.Integer)
    
    def __init__(self, id, nome, disciplina):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina
        

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "disciplina": self.disciplina}
    

class Alunos(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    nome = db.Collumn(db.String(100))
    idade = db.Collumn(db.Integer)
    turma_id = db.Collumn(db.Integer)

    def __init__(self, nome, idade, turma_id, id = None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id

    def to_dict(self):
        return{"id": self.id, "nome": self.nome, "idade": self.idade, "turma_id": self.turma_id}
    

class Turmas(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    nome = db.Collumn(db.String(100))
    professor_id = db.Collumn(db.Integer)

    def __init__(self, id, nome, professor_id):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "professor_id": self.professor_id}    