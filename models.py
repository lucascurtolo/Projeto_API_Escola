class Professores:
    def __init__(self, id, nome, materia):
        self.id = id
        self.nome = nome
        self.materia = materia

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "materia": self.materia}
    

class Alunos:
    def __init__(self, id, nome, idade):
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