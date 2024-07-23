from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Voluntario, Doacao

@app.before_first_request
def create_tables():
    if not os.path.exists('database.db'):
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_voluntario', methods=['POST'])
def cadastrar_voluntario():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    novo_voluntario = Voluntario(nome=nome, email=email, telefone=telefone)
    db.session.add(novo_voluntario)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/cadastrar_doacao', methods=['POST'])
def cadastrar_doacao():
    doador = request.form['doador']
    valor = request.form['valor']
    data = request.form['data']
    nova_doacao = Doacao(doador=doador, valor=valor, data=data)
    db.session.add(nova_doacao)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
