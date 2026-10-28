from flask import request, render_template, render_template_string
from models.venda import Venda


def cadastrar():
    produto = request.form["produto"]
    quantidade = request.form["quantidade"]
    preco = request.form["preco"]
    venda = Venda(produto, quantidade, preco)
    id_venda = venda.salva()


    return f"Venda do produto '{venda.produto}' cadastrada com sucesso! ID: {id_venda}"

def listar():
    lista_vendas = Venda.listar()
    return render_template_string(""
    "<h1>vendas<h1><br>{{lista}}"
    , lista=lista_vendas)