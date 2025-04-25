from Config import app, db
from Controllers.alunos_routes import alunos_blueprint
from Controllers.turmas_routes import turmas_blueprint
from Controllers.professores_routes import professores_blueprint
import os

app.register_blueprint(alunos_blueprint, url_prefix="/alunos")
app.register_blueprint(professores_blueprint, url_prefix="/professores")
app.register_blueprint(turmas_blueprint, url_prefix="/turmas")

with app.app_context():
    print("Criando o banco de dados...")
    db.create_all()
    print("Banco criado em:", os.path.abspath("app.db"))

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
