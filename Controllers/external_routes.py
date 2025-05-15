from flask import Blueprint, jsonify
from clients.pessoa_service_client import PessoaServiceClient
from clients.atividade_service_client import AtividadeServiceClient

api_gateway_bp = Blueprint('api_gateway', __name__)

@api_gateway_bp.route('/professores')
def professores():
    return jsonify(PessoaServiceClient.get_professores())

@api_gateway_bp.route('/alunos')
def alunos():
    return jsonify(PessoaServiceClient.get_alunos())


@api_gateway_bp.route('/atividades')
def atividades():
    return jsonify(AtividadeServiceClient.get_atividades())

@api_gateway_bp.route('/atividades/<int:id_atividade>')
def atividade(id_atividade):
    atividade = AtividadeServiceClient.get_atividade(id_atividade)
    if atividade:
        return jsonify(atividade)
    return jsonify({'erro': 'Atividade não encontrada'}), 404

@api_gateway_bp.route('/leciona/<int:id_professor>/<int:id_disciplina>')
def leciona(id_professor, id_disciplina):
    return jsonify({'leciona': PessoaServiceClient.verificar_leciona(id_professor, id_disciplina)})
