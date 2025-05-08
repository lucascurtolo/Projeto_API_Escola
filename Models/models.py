from Config import db

class Professores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    disciplina = db.Column(db.Integer)
    idade = db.Column(db.Integer)

    turmas = db.relationship("Turmas", backref="professor", lazy=True)

    def __init__(self, nome, disciplina, idade, id=None):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina
        self.idade = idade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "disciplina": self.disciplina,
            "idade": self.idade
        }


class Turmas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))

    alunos = db.relationship("Alunos", backref="turma", lazy=True)

    def __init__(self, nome, professor_id, id=None):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "professor_id": self.professor_id
        }


class Alunos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))
    data_nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def __init__(self, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final, id=None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,
            "data_nascimento": self.data_nascimento,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.media_final
        }
