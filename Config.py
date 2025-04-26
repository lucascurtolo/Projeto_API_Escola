import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializando o banco de dados
db = SQLAlchemy()

# Função que cria o app
def create_app():
    app = Flask(__name__)
    app.config['HOST'] = '0.0.0.0'
    app.config['PORT'] = 8000
    app.config['DEBUG'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memory"  # Banco em memória
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrar as rotas (blueprints) aqui ou fora
    from Controllers.alunos_routes import alunos_blueprint
    from Controllers.turmas_routes import turmas_blueprint
    from Controllers.professores_routes import professores_blueprint

    # Registrando as rotas no app
    app.register_blueprint(alunos_blueprint, url_prefix="/alunos")
    app.register_blueprint(professores_blueprint, url_prefix="/professores")
    app.register_blueprint(turmas_blueprint, url_prefix="/turmas")

    return app
