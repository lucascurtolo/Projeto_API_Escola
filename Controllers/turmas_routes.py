from flask import Blueprint, request, jsonify
from Models.turmas import TurmasModel, Turmas

turmas_blueprint = Blueprint('turmas', __name__)
turmas_repo = TurmasModel()

@turmas_blueprint.route("/", methods = ["POST"])
def criar_turma_route():
    data = request.get_json()
    try:
        turma = Turmas(**data)
        turmas_repo.criar_turma(turma)
        return jsonify(turma.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro":str(e)}), 400


@turmas_blueprint.route("/<int:id>", methods = ["GET"])
def listar_turma_route(id):
    try:
        turma = turmas_repo.listar_turma(id)
        return jsonify(turma.to_dict()), 200
    except ValueError:
        return jsonify({"erro": "Turma não encontrada"}), 400


@turmas_blueprint.route("/", methods = ["GET"])
def listar_todas_turmas_route():
    try:
        turmas = turmas_repo.listar_todas_turmas()
        return jsonify([tur.to_dict() for tur in turmas]), 200
    except ValueError:
        return jsonify({"message": "Turma não encontrada"}), 400


@turmas_blueprint.route("/<int:id>", methods = ["DELETE"])
def excluir_turma_route(id):
    try:
        turma = turmas_repo.excluir_turma(id)
        return '', 204
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404


@turmas_blueprint.route("/", methods = ["DELETE"])
def excluir_todas_turmas_route():
    try:
        turmas = turmas_repo.excluir_todas_turmas()
        return '', 204
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404


@turmas_blueprint.route("/<int:id>", methods = ["PUT"])
def atualizar_turma_route(id):
    data = request.get_json()
    try:
        professor_id = data.get("professor_id")
        nome = data.get("nome")
        turma = turmas_repo.atualizar_turma(id, nome, professor_id)
        return jsonify(turma.to_dict()), 200
    except ValueError:
        return jsonify({"erro": "Turma não encontrada"}), 404







