from database import conectar
from models.venda import Venda

class Venda:

    def __init__(self, produto, quantidade, preco, venda):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
        self.venda = venda
    def salva(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """INSERT INTO venda (produto, quantidade, preco)
        VALUES (?, ?, ?)"""
        valores = (self.produto, self.quantidade, self.preco)

        cursor.execute(sql, valores)
        conexao.commit()

        lastrowid = cursor.lastrowid

        cursor.close()
        conexao.close()
        return lastrowid

    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM venda")
        lista_vendas = cursor.fetchall()
        cursor.close()
        conexao.close()

        return lista_vendas