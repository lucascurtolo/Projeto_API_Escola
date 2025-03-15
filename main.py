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

@app.route("/alunos/<int:id>", methods = ["GET"])
def listar_alunos(id):
    for aluno in alunos_db:
        if aluno.id == id:
            return jsonify({"id": aluno.id, "nome": aluno.nome, "idade": aluno.idade})
    return jsonify({"message": "Aluno não encontrado"})

@app.route("/alunos_list", methods = ["GET"])
def listar_todos_alunos():
    alunos_list = [aluno.to_dict() for aluno in alunos_db]
    qtd_alunos = len(alunos_db)
    if qtd_alunos == 0:
        return jsonify({"mensagem": "Alunos não encontrados"})
    else:
        return jsonify(alunos_list), 200


if __name__ == "__main__":
    app.run()