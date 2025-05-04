

from swagger.namespaces import api
from swagger.namespaces.aluno_namespace import api as alunos_api
from swagger.namespaces.professor_namespace import api as professores_api
from swagger.namespaces.turma_namespaces import api as turmas_api

def configure_swagger(app):
    api.init_app(app)  

    api.add_namespace(alunos_api)
    api.add_namespace(professores_api)
    api.add_namespace(turmas_api)
   