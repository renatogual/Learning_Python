'''Faça um programa que leia um nome de usuário e a sua senha e não
aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
e voltando a pedir as informações.'''

loguin = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

while True:
    if senha == loguin:
        senha = input("A senha nao pode ser igual ao loguin, digite novamente: ")
    else:
        break
