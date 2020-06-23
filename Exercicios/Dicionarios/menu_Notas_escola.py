# Uma escola te contratou para fazer um software em Python.
# Eles querem que você crie um script que exiba o seguinte menu:

# 0. Sair
# 1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
# 2. Inserir aluno e nota
# 3. Alterar a nota de um aluno
# 4. Consultar nota de um aluno específico
# 5. Apagar um aluno da lista
# 6. Dar a média da turma

# Onde a professora que vai fornecer o nome e nota dos alunos. Quantos ela quiser. Quantas vezes quiser.
# Implemente esse script usando um dicionário.

notas = {}

def menu():
    print("0. Sair")
    print("1. Exibir Lista de alunos com suas notas")
    print("2. Inserir aluno e nota")
    print("3. Alterar a nota de um aluno")
    print("4. Consultar nota de um aluno específico")
    print("5. Apagar um aluno da lista")
    print("6. Dar a média da turma")


def ExibirLista():
    for nome in notas.keys():
        print(nome, "Tirou a nota: ", notas[nome])


def InserirAluno():
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Nota dele: "))

    if notas.get(nome):
        print("Ja existe o aluno ", nome)
    else:
        notas[nome] = nota


def AlterarNota():
    nome = input("Aluno a mudar a nota: ")
    nota = float(input("Nova nota     : "))

    if nome in notas.keys():
        notas[nome] = nota
    else:
        print("Não existe esse aluno")


def ConsultaNota():
    nome = input("Aluno a ser consultada a nota: ")

    if notas.get(nome) == None:
        print("Nao existe o aluno: ", nome)
    else:
        print(nome, "Tirou a nota ", notas[nome])


def ApagarAluno():
    nome = input("Qual aluno deverá ser apagado: ")
    notas.pop(nome)


def media():
    soma = 0
    for count in notas.values():
        soma += count
    print("Média dos alunos: %.2f" % (soma / len(notas)))

a = 1

while a:
    print()
    menu()
    escolha = int(input("Digite a opção desejada: "))
    if escolha == 0:
        a = 0
    if escolha == 1:
        print()
        ExibirLista()
    elif escolha == 2:
        print()
        InserirAluno()
    elif escolha == 3:
        print()
        AlterarNota()
    elif escolha == 4:
        print()
        ConsultaNota()
    elif escolha == 5:
        print()
        ApagarAluno()
    elif escolha == 6:
        print()
        media()




