from Config import app
import os 

from Controllers.alunos_routes import alunos_blueprint
from Controllers.turmas_routes import turmas_blueprint
from Controllers.professores_routes import professores_blueprint

app.register_blueprint(alunos_blueprint, url_prefix="/alunos")
app.register_blueprint(professores_blueprint, url_prefix="/professores")
app.register_blueprint(turmas_blueprint, url_prefix="/turmas")

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
