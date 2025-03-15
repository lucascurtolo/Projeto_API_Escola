from flask import Flask, json, request, jsonify
from models import *

app = Flask(__name__)

alunos_db = [
    Alunos(id = 5, nome= "Marcelo", idade = 19),
    Alunos(id = 8, nome = "Lucas", idade = 20)
]

turmas_db = [
    Turmas(id = 3, nome = "3A", professor_id= 8),
    Turmas(id = 5, nome = "3B", professor_id= 5)
]

professores_db = [
    Professores(id = 8, nome = "Caio", disciplina = "Desenvolvimento de Apis"),
    Professores(id = 5, nome = "Lucio", disciplina = "Lógica de Programação")
]

@app.route("/alunos", methods = ["POST"])
def criar_aluno():
     data = request.get_json()
     aluno = Alunos(id = data["id"], nome = data["nome"], idade = data["idade"])
     alunos_db.append(aluno)
     return jsonify(aluno.to_dict()), 201


if __name__ == "__main__":
    app.run()