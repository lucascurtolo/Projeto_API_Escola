from flask_restx import Namespace, Resource, fields
from Models.alunos import Alunos_Repository
from datetime import datetime, date
aluno_repo = Alunos_Repository()

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos")

# Exporta o namespace com o nome 'api'
api = alunos_ns

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

alunos_model = alunos_ns.model("Aluno", {
    "id": fields.Integer(required=False, description="ID do Aluno (opcional)"),
    "nome": fields.String(required=True, description="Nome do Aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (formato YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=False, description="ID da Turma (opcional)")
})

alunos_output_model = alunos_ns.model("AlunosOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento"),
    "nota_primeiro_semestre": fields.Float(description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(description="Nota do segundo semestre"),
    "media_final": fields.Float(description="Média final"),
    "turma_id": fields.Integer(description="ID da turma associada")
})


@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(alunos_output_model)
    def get(self):
        return aluno_repo.listar_todos_alunos()
    
    
    def delete(self):
        aluno_repo.excluir_todos_alunos()
        return {"message": "Alunos excluídos"}, 200
    
    @alunos_ns.expect(alunos_model)
    def post(self):
        """
        Cria um novo aluno
        """
        try:
            data = alunos_ns.payload
            
            aluno = aluno_repo.criar_aluno(
                id=data.get('id'),
                nome=data['nome'],
                data_nascimento_str=data['data_nascimento'],
                nota_primeiro_semestre=data['nota_primeiro_semestre'],
                nota_segundo_semestre=data['nota_segundo_semestre'],
                turma_id=data.get('turma_id')  # Opcional
            )
            
            return aluno.to_dict(), 201
            
        except ValueError as e:
            alunos_ns.abort(400, str(e))
        except Exception as e:
            alunos_ns.abort(500, f"Erro interno do servidor: {str(e)}")
    

@alunos_ns.route("/<int:id>")  # <- corrigido aqui
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(alunos_output_model)
    def get(self, id):
        return aluno_repo.listar_aluno(id)
    
    @alunos_ns.expect(alunos_model)
    def put(self, id):
        """
        Atualiza um aluno pelo ID
        """
        try:
            # Verificar se o aluno existe
            aluno_existente = aluno_repo.listar_aluno(id)
            if not aluno_existente:
                alunos_ns.abort(404, f"Aluno com ID {id} não encontrado")
            
            data = alunos_ns.payload

            data_nascimento_str = data.get('data_nascimento')
            
            if data_nascimento_str and not validate_date_format(data_nascimento_str):
                alunos_ns.abort(400, "Formato de data inválido. Use o formato YYYY-MM-DD (ex: 2005-07-15)")

            data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
            
            aluno = aluno_repo.atualizar_aluno(
                id=id,
                nome=data.get('nome'),
                data_nascimento=data_nascimento,
                nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
                nota_segundo_semestre=data.get('nota_segundo_semestre'),
                turma_id=data.get('turma_id')
            )
            
            return aluno.to_dict(), 200
            
        except ValueError as e:
            alunos_ns.abort(400, str(e))
        except Exception as e:
            alunos_ns.abort(500, f"Erro interno do servidor: {str(e)}")
    
    def delete(self, id):
        aluno_repo.excluir_aluno(id)
        return {"message": "Aluno excluído"}, 200