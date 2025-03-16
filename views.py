from main import app
from flask import render_template, request,redirect
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
   
    session.add(Usuario(
        nome=request.form['nome'], 
        email=request.form['email'], 
        senha=request.form['senha']
    ))
    session.commit()
    return redirect('/usuarios/registar')

    # adicionar um usuario a base de dados
    request.form['nome']
    request.form['email']
    request.form['senha']
    # retornar a pagina de registo
@app.route('/usuarios/registar')
def usuarios(name_user):
    return
    # adicionar um usuario a base de dados
    

    

@app.route('/usuarios/login')
def login():
    return render_template("./login.html")

@app.post('/usuarios/login')
def login_post():
    loginuser = session.query(Usuario).where(Usuario.email == request.form['email'] and  Usuario.senha == request.form['senha']).one_or_none()
    if not loginuser:
        return redirect('/usuarios')
    
    print("user logged in")

    randomuser = session.query(Usuario).where(Usuario.nome != loginuser.nome).order_by(func.random()).limit(1).one_or_none()
    
    print("randomuser", randomuser)

    return render_template("./usuarios.html", name_user=randomuser.nome)
    # verificar se o usuario existe na base de dados
    request.form['email']
    # verificar se a senha esta correta
    request.form['senha']
    # retornar a pagina de login

@app.post('/usuarios/logout')
def logout():
    return redirect('/')