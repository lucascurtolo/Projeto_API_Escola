from flask import Blueprint, request, jsonify
from Models.alunos import Alunos_Repository
from Models.alunos import Alunos_Repository, Alunos
from datetime import datetime
from Models.models import Alunos


alunos_blueprint = Blueprint('alunos', __name__)
alunos_repo = Alunos_Repository()

@alunos_blueprint.route("/", methods=["POST"])
def criar_aluno_route():
    data = request.get_json()
    try:
        id = data["id"]
        nome = data["nome"]
        data_nascimento_str = data["data_nascimento"] 
        turma_id = data["turma_id"]
        nota_primeiro_semestre = data["nota_primeiro_semestre"]
        nota_segundo_semestre = data["nota_segundo_semestre"]

        
        aluno = alunos_repo.criar_aluno(id, nome, data_nascimento_str, nota_primeiro_semestre, nota_segundo_semestre, turma_id)
        
        
        return jsonify(aluno.to_dict()), 201
    except (ValueError, KeyError) as e:
        return jsonify({"erro": str(e)}), 400



@alunos_blueprint.route("/<int:id>", methods=["GET"])
def listar_aluno_route(id):
        aluno = alunos_repo.listar_aluno(id)
        if aluno is None:
            return jsonify({"message": "Aluno não encontrado"}), 404
        return jsonify(aluno.to_dict())

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

@alunos_blueprint.route("/", methods=["DELETE"])
def excluir_todos_alunos_route():
    try:
        alunos = alunos_repo.excluir_todos_alunos()
        return '', 204
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404


@alunos_blueprint.route("/<int:id>", methods=["PUT"])
def atualizar_aluno_route(id):
    data = request.get_json()
    try:
        nome = data.get("nome")
        idade = data.get("idade")
        turma_id = data.get("turma_id")
        data_nascimento_str = data.get("data_nascimento")
        nota_primeiro_semestre = data.get("nota_primeiro_semestre")
        nota_segundo_semestre = data.get("nota_segundo_semestre")
        media_final = data.get("media_final")

        # ⚠️ Converte string para date
        data_nascimento = None
        if data_nascimento_str:
            try:
                data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
            except ValueError:
                data_nascimento = datetime.strptime(data_nascimento_str, "%a, %d %b %Y %H:%M:%S GMT").date()

        aluno = alunos_repo.atualizar_aluno(
            id, nome, idade, turma_id, data_nascimento,
            nota_primeiro_semestre, nota_segundo_semestre, media_final
        )
        return jsonify(aluno.to_dict())

    except ValueError:
        return jsonify({"message": "Aluno não encontrado"}), 404

    