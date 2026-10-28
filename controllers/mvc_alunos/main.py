from flask import Flask
from mvc_loja.controllers.mvc_alunos.controllers.aluno_controller import formulario
from mvc_loja.controllers.mvc_alunos.controllers.aluno_controller import cadastrar
from mvc_loja.controllers.mvc_alunos.controllers.aluno_controller import listar 
from mvc_loja.controllers.mvc_alunos.controllers.aluno_controller import apagar

app = Flask(__name__)

@app.route("/")
def inicio():
    return formulario()

@app.route("/aluno", methods=["POST"]) 
def salvar_aluno():
    return cadastrar()


@app.route("/alunos")
def listar_alunos():
    return listar()

@app.route("/aluno/deletar/<int:id>")
def excluir_aluno(id):
    return apagar(id)

app.run(debug=True)