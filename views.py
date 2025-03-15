from main import app
from flask import render_template


@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/contactos')
def contactos():
    return render_template("./contactos.html")

@app.route('/usuarios/<name_user>')
def usuarios(name_user):
    return render_template("./usuarios.html", name_user=name_user)