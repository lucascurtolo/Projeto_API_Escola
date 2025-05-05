from flask_restx import Namespace, Resource, fields
from Models.turmas import Turmas_Repository
turmas_repo = Turmas_Repository()

turmas_ns = Namespace("turmas", description="Operações relaciondas a turma")

api = turmas_ns

turmas_model = turmas_ns.model("Turma", {
    "nome": fields.String(required = True, description= "Nome da Turma"),
    "professor_id": fields.String(required = True, description= "Id do Professor da turma")
})

turmas_output_model = turmas_ns.model("TurmasOutput", {
    "id": fields.Integer(description="Id da turma"),
    "nome": fields.String(description="Nome da turma"),
    "turma_id": fields.Integer(description= "Id do professor da turma")
})


@turmas_ns.route("/")
class TurmaResource(Resource):
    @turmas_ns.marshal_with(turmas_output_model)
    def get(self):
        return turmas_repo.listar_todas_turmas()
    
    def delete(self):
        turmas_repo.excluir_todas_turmas()
        return {"message": "Turmas excluídas"}
    
    @turmas_ns.expect(turmas_model)
    def post(self):
        data = turmas_ns.payload
        response, status_code = turmas_repo.criar_turma(data)
        return response, status_code

@turmas_ns.route("/<int:id>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_list_with(turmas_output_model)
    def get(self,id):
        return turmas_repo.listar_turma()
    
    @turmas_ns.expect(turmas_model)
    def put(self,id):
        data = turmas_ns.payload
        turmas_repo.atualizar_turma(id, data)
        return data, 200
    
    def delete(self,id):
        turmas_repo.excluir_turma(id)
        return {"message": "Turmas excluídas"}, 200