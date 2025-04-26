from Config import create_app, db

app = create_app()

try:
    with app.app_context():
        db.create_all()
    print("Tabelas criadas com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
