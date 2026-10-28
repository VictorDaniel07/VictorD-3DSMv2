from flask import Blueprint, render_template, session, abort

sistema = Blueprint("sistema",__name__)

@sistema.route("/home")
def home():
    return render_template("home.html")

@sistema.route("/produtos")
def produtos():
    if session["usuario"]["permissao"] == "produtos":
        return render_template("produtos.html")
    else:
        abort(403)

@sistema.route("/relatorios")
def relatorios():
    if session["usuario"]["permissao"] == "relatorios":
        return render_template("relatorio.html")
    else:
        abort(403)