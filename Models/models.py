class Professores:
    def __init__(self, id, nome, disciplina):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "disciplina": self.disciplina}
    

class Alunos:
    def __init__(self, nome, idade, id = None):
        self.id = id
        self.nome = nome
        self.idade = idade

    def to_dict(self):
        return{"id": self.id, "nome": self.nome, "idade": self.idade}
    

class Turmas:
    def __init__(self, id, nome, professor_id):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "professor_id": self.professor_id}    