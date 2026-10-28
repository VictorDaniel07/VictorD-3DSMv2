from mvc_loja.controllers.mvc_alunos.models.aluno import Aluno
import mvc_loja.controllers.mvc_alunos.view as view

class AlunoController:
    def cadastrar(self):
        nome = view.pedir_nome()
        idade = view.pedir_idade()
        aluno = Aluno(nome, idade)
        aluno.matricular_aluno()
        view.mostrar_aluno(aluno)

    def listar(self):
        alunos = Aluno.listar()
        view.mostrar_alunos(alunos)

    def apagar(self, id):
        Aluno.apagar(id)
        print(f"Aluno com ID {id} foi apagado com sucesso.")