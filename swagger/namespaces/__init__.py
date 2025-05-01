from flask_restx import Api

# Crie a instância da API, mas NÃO associe a nenhum app Flask ainda
api = Api(
    version="1.0",
    title="API de Gestão Escolar",
    description="Documentação da API para Alunos, Professores e Turmas",
    doc="/docs",
    prefix="/api"
)

# Não importe namespaces nem outros módulos aqui para evitar importação circular



