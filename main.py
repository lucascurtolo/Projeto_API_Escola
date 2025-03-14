from flask import Flask, json, request, jsonify
from models import *

app = Flask(__name__)

alunos_db = [
    Alunos(id = 5, nome= "Marcelo", idade = 19),
    Alunos(id = 8, nome = "Lucas", idade = 20)
]

turmas_db = [
    Turmas(id = 3, nome = "3A", professor_id= 8),
    Turmas(id = 5, nome = "3B", professor_id= 5)
]

professores_db = [
    Professores(id = 8, nome = "Caio", disciplina = "Desenvolvimento de Apis"),
    Professores(id = 5, nome = "Lucio", disciplina = "Lógica de Programação")
]


if __name__ == "__main__":
    app.run()