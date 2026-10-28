from models.usuario import autenticar
from flask import Blueprint, request, render_template, session, redirect

auth = Blueprint("auth",__name__)

@auth.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        login = request.form["login"]
        senha = request.form["senha"]
        usuario = autenticar(login, senha)
        if usuario:
            session["usuario"] = usuario
            return redirect("/home")
        return render_template(
            "login.html",
            erro="Usuário ou senha incorretos"
        )
