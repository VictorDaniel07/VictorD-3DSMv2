from flask import Flask
from controllers.venda_controller import formulario
from controllers.venda_controller import cadastrar
from database import criar_tabela

app = Flask(__name__)

criar_tabela()

@app.route("/")
def inicio():
    return formulario()

@app.route("/venda", methods=["POST"])
def registrar_venda():
    return cadastrar()

app.run(debug=True)

