from flask_restx import Namespace, Resource, fields
from Models.alunos import Alunos_Repository
aluno_repo = Alunos_Repository()

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos")

# Exporta o namespace com o nome 'api'
api = alunos_ns

alunos_model = alunos_ns.model("Aluno", {
    "nome": fields.String(required=True, description="Nome do Aluno"),
    "idade": fields.Integer(required=True, description="Idade"),
    "turma_id": fields.Integer(required=True, description="ID da Turma")
})

alunos_output_model = alunos_ns.model("AlunosOutput", {
    "id": fields.Integer(description="ID aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "turma_id": fields.Integer(description="ID da turma associada")
})


@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(alunos_output_model)
    def get(self):
        return listar_todos_alunos()
    
    
    def delete(self):
        excluir_todos_alunos()
        return {"message": "Alunos excluídos"}, 200
    
    @alunos_ns.expect(alunos_model)
    def post(self):
        data = alunos_ns.payload
        response, status_code = criar_aluno(data)
        return response, status_code
    

@alunos_ns.route("/<int:id>")  # <- corrigido aqui
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(alunos_output_model)
    def get(self, id):
        return listar_aluno(id)
    
    @alunos_ns.expect(alunos_model)
    def put(self, id):
        data = alunos_ns.payload
        atualizar_aluno(id, data)
        return data, 200
    
    def delete(self, id):
        excluir_aluno(id)
        return {"message": "Aluno excluído"}, 200
