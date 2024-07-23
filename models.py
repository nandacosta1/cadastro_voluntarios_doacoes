from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Voluntario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

class Doacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doador = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.Date, nullable=False)
