from flask import Flask

from Routes.alunos_routes import alunos_blueprint
# from Routes.professores_routes import professores_blueprint
# from Routes.turmas_routes import turmas_blueprint

app = Flask(__name__)


app.register_blueprint(alunos_blueprint, url_prefix="/alunos")