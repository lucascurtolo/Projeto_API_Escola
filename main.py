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

@app.route("/alunos/<int:id>", methods = ["DELETE"])
def excluir_aluno(id):
    for aluno in alunos_db:
        if aluno.id == id:
            aluno_to_delete = aluno
            alunos_db.remove(aluno_to_delete)
    return jsonify({"message": "Aluno Excluído"})

@app.route("/alunos_list", methods = ["DELETE"])
def excluir_todos_alunos():
    alunos_db.clear()
    return jsonify({"mensagem": "Alunos removidos com sucesso"})

@app.route("/alunos/<int:id>", methods = ["PUT"])
def atualizar_aluno(id):
    qtd_alunos = len(alunos_db)
    if qtd_alunos == 0:
        return jsonify({"mensagem": "Alunos não encontrados"})
    else:
        for aluno in alunos_db:
            if aluno.id == id:
                nome_aluno = request.get_json()
                aluno.nome = nome_aluno.get("nome", aluno.nome)
                return jsonify({"mensagem": "Aluno atualizado"})
            


@app.route("/turmas", methods = ["POST"])
def criar_turma():
    data = request.get_json()
    turma = Turmas(id = data["id"], nome = data["nome"], professor_id = data["professor_id"])
    turmas_db.append(turma)
    return jsonify(turma.to_dict()),201

@app.route("/turmas/<int:id>", methods = ["GET"])
def listar_turmas(id):
    for turma in turmas_db:
        if turma.id == id:
            return jsonify({"id": turma.id, "nome": turma.nome, "professsor_id": turma.professor_id})
    return jsonify({"message": "Turma não encontrada"})

@app.route("/turmas_list", methods = ["GET"])
def listar_todas_turmas():
    turmas_list = [turma.to_dict() for turma in turmas_db]
    qtd_turmas = len(turmas_db)
    if qtd_turmas == 0 :
        return jsonify({"mensagem": "Turmas não encontradas"})
    else:
        return jsonify(turmas_list)
    
@app.route("/turmas/<int:id>", methods = ["DELETE"])
def excluir_turma(id):
    for turma in turmas_db:
        if turma.id == id:
            turma_to_delete = turma
            turmas_db.remove(turma_to_delete)
        return jsonify({"message": "Turma excluída"})    

@app.route("/turmas_list", methods = ["DELETE"])
def excluir_todas_turmas():
    turmas_db.clear()
    return jsonify({"mensagem": "Turmas excluídas"})
    
@app.route("/turmas/<int:id>", methods = ["PUT"])
def atualizar_turma(id):
    qtd_turmas = len(turmas_db)
    if qtd_turmas == 0:
        return jsonify({"mensagem": "Turma não encontrada"})
    else:
        for turma in turmas_db:
            if turma.id == id:
                nome_turma = request.get_json()
                turma.nome = nome_turma.get("nome", turma.nome)
                return jsonify({"mensagem": "Turma atualizada"})

@app.route("/professores", methods = ["POST"])
def criar_professor():
    data = request.get_json()
    professor = Professores(id = data["id"], nome = data["nome"], disciplina = data["disciplina"])
    professores_db.append(professor)
    return jsonify(professor.to_dict()), 201

@app.route("/professores/<int:id>", methods = ["GET"])
def listar_professores(id):
    for professor in professores_db:
        if professor.id == id:
            return jsonify({"id": professor.id, "nome": professor.nome, "disciplina": professor.disciplina})
    return jsonify({"message": "Professor não encontrado"})
 
@app.route("/professores_list", methods = ["GET"])
def listar_todos_professores():
    professores_list = [professor.to_dict() for professor in professores_db]
    qtd_professores = len(professores_db)
    if qtd_professores == 0:
        return jsonify({"mensagem": "Professores não encontrados"})
    else:
        return jsonify(professores_list), 200

if __name__ == "__main__":
    app.run()