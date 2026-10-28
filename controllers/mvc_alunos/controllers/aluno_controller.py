from flask import request, render_template
from mvc_loja.controllers.mvc_alunos.models.aluno import Aluno

def formulario():
    return render_template("formulario.html")

def cadastrar():
    nome = request.form["nome"]
    idade = request.form["idade"]
    aluno = Aluno(nome, idade)
    aluno.salvar()
    return render_template(
        "sucesso.html",
        nome=nome
    )

def listar():
    alunos = Aluno.listar()
    return render_template(
        "lista.html", 
        alunos=alunos
    )
def apagar(id):
    Aluno.apagar(id)
    return render_template(
        "deletado.html",
        id=id
    )