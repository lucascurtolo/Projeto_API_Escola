from Config import create_app, db
from swagger.swagger_config import configure_swagger  # Importa a função para configurar o Swagger

# Criação do app
app = create_app()

# Configura o Swagger
configure_swagger(app)

# Criação das tabelas do banco
try:
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    print("Tabelas criadas com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Executando a aplicação
if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
