from mvc_loja.controllers.mvc_alunos.database import conectar

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.matriculado = False
        self.maior = False

    def me_matricular(self):
        if self.maior:
            self.matriculado = True

    def verificar_maioridade(self):
        if self.idade >= 18:
            self.maior = True
            return "Maior de Idade"
        else:
            self.maior = False
            return "Menor de Idade"

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """INSERT INTO aluno (nome, idade)
        VALUES (%s, %s)"""
        valores = (self.nome, self.idade)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM aluno"
        cursor.execute(sql)
        alunos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return alunos

    def apagar(id):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM aluno WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        cursor.close()
        conexao.close()