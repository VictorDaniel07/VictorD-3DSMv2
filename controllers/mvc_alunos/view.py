def pedir_nome():
    return input("Digite o nome: ")

def pedir_idade():
    return int(input("Digite a idade: "))

def mostrar_aluno(aluno):
    print("Nome: ", aluno.nome)
    print("Idade: ", aluno.idade)
    print("Matriculado", aluno.matriculado)
    print("Situação:", aluno.verificar_maioridade())

