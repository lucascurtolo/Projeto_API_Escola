from flask import Blueprint, request, jsonify
from Models.alunos import Alunos_Repository
from Models.alunos import Alunos_Repository, Alunos


alunos_blueprint = Blueprint('alunos', __name__)
alunos_repo = Alunos_Repository()

@alunos_blueprint.route("/", methods=["POST"])
def criar_aluno_route():
    data = request.get_json()
    try:
        aluno = alunos_repo.criar_aluno(data['nome'], data['idade'], data['turma_id'])
        return jsonify(aluno.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@alunos_blueprint.route("/<int:id>", methods=["GET"])
def listar_aluno_route(id):
    try:
        aluno = alunos_repo.listar_aluno(id)
        return jsonify(aluno.to_dict())
    except ValueError:
        return jsonify({"message": "Aluno não encontrado"}), 404

@alunos_blueprint.route("", methods=["GET"])
def listar_todos_alunos_route():
    try:
        alunos = alunos_repo.listar_todos_alunos()
        return jsonify([aluno.to_dict() for aluno in alunos]),200
    except ValueError:
        return jsonify({"message": "Alunos não encontrados"}), 404    

@alunos_blueprint.route("/<int:id>", methods=["DELETE"])
def excluir_aluno_route(id):
    try:
        alunos_repo.excluir_aluno(id)
        return '', 204
    except ValueError:
        return jsonify({"message": "Aluno não encontrado"}), 404

@alunos_blueprint.route("", methods=["DELETE"])
def excluir_todos_alunos_route():
    try:
        alunos_repo.excluir_todos_alunos()
        return jsonify({"mensagem": "Alunos removidos com sucesso"}), 204
    except ValueError:
        return jsonify({"message": "Alunos não encontrados"}), 404

@alunos_blueprint.route("/<int:id>", methods=["PUT"])
def atualizar_aluno_route(id):
    data = request.get_json()
    try:
        nome = data.get("nome")
        idade = data.get("idade")
        turma_id = data.get("turma_id")
        aluno = alunos_repo.atualizar_aluno(id, nome, idade, turma_id)
        return jsonify(aluno.to_dict())
    except ValueError:
        return jsonify({"message": "Aluno não encontrado"}), 404

    
