from flask_restx import Namespace, Resource, fields
from Models.turmas import Turmas_Repository
turmas_repo = Turmas_Repository()

turmas_ns = Namespace("turmas", description="Operações relaciondas a turma")

api = turmas_ns

turmas_model = turmas_ns.model("Turma", {
    "nome": fields.String(required = True, description= "Nome da Turma"),
    "professor_id": fields.Integer(required = True, description= "Id do Professor da turma")
})

turmas_output_model = turmas_ns.model("TurmasOutput", {
    "id": fields.Integer(description="Id da turma"),
    "nome": fields.String(description="Nome da turma"),
    "professor_id": fields.Integer(description= "Id do professor da turma")
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
        nome = data['nome']
        professor_id = data['professor_id']

        turma = turmas_repo.criar_turma(id=None ,nome=nome, professor_id=professor_id)

        return turma.to_dict(), 201

@turmas_ns.route("/<int:id>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_list_with(turmas_output_model)
    def get(self,id):
        turma = turmas_repo.listar_turma(id)
        if turma:
            return turma.to_dict(), 200
        else:
            return {"message": "Turma não encontrada"}, 404
    
    @turmas_ns.expect(turmas_model) 
    def put(self, id):
        data = turmas_ns.payload
        nome = data["nome"]
        professor_id = data["professor_id"]
        turma =  turmas_repo.atualizar_turma(id=id, nome=nome, professor_id=professor_id)
        return turma.to_dict(), 200
    
    def delete(self,id):
        turmas_repo.excluir_turma(id)
        return {"message": "Turmas excluídas"}, 200