from main import app
from flask import render_template, request
from main2 import session, Usuario
from  sqlalchemy.sql.expression import func, select


@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/contactos')
def contactos():
    return render_template("./contactos.html")

@app.route('/usuarios/registar')
def registar_render():
    return render_template("./registar.html")

@app.post('/usuarios/registar')
def registar():
    request.form['nome']
    session.add(Usuario(nome='name_user', email="dad@asd.com", senha="123", telefone="123", endereco="rua", cidade="cidade"))
    session.commit()

@app.route('/usuarios/registar')
def usuarios(name_user):
    # adicionar um usuario a base de dados
    

    # vai buscar um usuario aleatorio
    session.query(Usuario).order_by(func.random).limit(1).one_or_none()

    # faaz login com senha e password
    session.query(Usuario).where(Usuario.nome == 'nome para verificar' & Usuario.senha == 'senha a verificar').one_or_none()
    return render_template("./usuarios.html", name_user=name_user)