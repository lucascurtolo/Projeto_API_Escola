from flask_restx import Namespace, Resource, fields
from Models.professores import Professores_Repository
professores_repo = Professores_Repository()

professores_ns = Namespace("professores", description="Operações relacionadas a professor")
api = professores_ns

professores_model = professores_ns.model("Professor",{
    "nome": fields.String(required = True, description= "Nome do Professor"),
    "disciplina": fields.String(required = True, description= "Disciplina do Professor"),
    "idade": fields.Integer(required =True, description= "Idade do Professor")
})

professores_output_model = professores_ns.model("ProfessoresOutput",{
    "id": fields.Integer(description= "ID do Professor"),
    "nome": fields.String(description="Nome do Professor"),
    "disciplina": fields.String(description="Nome da Disciplina"),
    "idade": fields.Integer(description="Idade do Professor")
})


@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professores_output_model)
    def get(self):
       return professores_repo.listar_todos_professores()
            
    
    def delete(self):
        professores_repo.excluir_todos_professores()
        return {"message": "Professores excluídos"}
    
    @professores_ns.expect(professores_model)
    def post(self):
        data = professores_ns.payload
        nome = data['nome']
        disciplina = data['disciplina']
        idade = data['idade']

        professor = professores_repo.criar_professor(id=None ,nome=nome, disciplina=disciplina, idade=idade)

        return professor.to_dict(), 201
    
@professores_ns.route("/<int:id>")
class ProfessorIdResource(Resource):
    @professores_ns.marshal_list_with(professores_output_model)
    def get(self, id):
        professor = professores_repo.listar_professor(id)
    
        if professor:
            return professor.to_dict(), 200
        else:
            return {'erro': 'Professor não encontrado'}, 404
    
    @professores_ns.expect(professores_model)
    def put(self, id):
        data = professores_ns.payload
        nome = data["nome"]
        disciplina = data["disciplina"]
        idade = data["idade"]
        professor =  professores_repo.atualizar_professores(id=id, nome=nome, disciplina=disciplina, idade=idade)
        return professor.to_dict(), 200
    
    def delete(self, id):
        professores_repo.excluir_professores(id)
        return {"message": "Professor excluído"}, 200