from flask import Blueprint, request, jsonify
from Models.professores import ProfessoresRepository, Professores

professores_blueprint = Blueprint('professores', __name__)
professores_repo = ProfessoresRepository()

@professores_blueprint.route("/", methods=["POST"])
def criar_professor_route():
    data = request.get_json()
    try:
        professor = Professores(**data)
        professores_repo.criar_professor(professor)
        return jsonify(professor.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@professores_blueprint.route("/<int:id>", methods=["GET"])
def listar_professor_route(id):
    try:
        professor = professores_repo.listar_professor(id)
        return jsonify(professor.to_dict())
    except ValueError:
        return jsonify({"message": "Professor não encontrado"}), 404

@professores_blueprint.route("/", methods=["GET"])
def listar_todos_professores_route():
    try:
        professores = professores_repo.listar_todos_professores()
        return jsonify([prof.to_dict() for prof in professores])
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

@professores_blueprint.route("/<int:id>", methods=["DELETE"])
def excluir_professor_route(id):
    try:
        professores_repo.excluir_professores(id)
        return '', 204
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

@professores_blueprint.route("", methods=["DELETE"])
def excluir_todos_professores_route():
    try:
        professores_repo.excluir_todos_professores()
        return '', 204
    except ValueError:
        return jsonify({"message": "Erro ao excluir professores"}), 404

@professores_blueprint.route("/<int:id>", methods=["PUT"])
def atualizar_professor_route(id):
    data = request.get_json()
    try:
        nome = data.get("nome")
        disciplina = data.get("idade")
        professor = professores_repo.atualizar_professores(id, nome, disciplina)
        return jsonify(professor.to_dict())
    except ValueError:
        return jsonify({"message": "Professor não encontrado"}), 404
