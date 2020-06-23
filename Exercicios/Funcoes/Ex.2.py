# Exercicio 2 de Funções
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma
# desses três argumentos através de uma função. Seu script também deve fornecer a média dos três números, através de
# uma segunda função que chama a primeira.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))


def soma(x, y, z):
    return x + y + z


def media():
    x = soma(num1, num2, num3) / 3
    return x


print("A soma desses numeros é: ", soma(num1, num2, num3))
print("A média desses numeros é: ", media())

