# Exercicio 3 de Funções
# Faça um programa que recebe três números do usuário, e identifica o maior através de uma
# função e o menor número através de outra função.

def maior(x, y, z):
    result = 0
    if x > y and x > z:
        result = x
    elif y > x and y > z:
        result = y
    elif z > x and z > y:
        result = z
    return result


def menor(x, y, z):
    result = 0
    if x < y and x < z:
        result = x
    elif y < x and y < z:
        result = y
    elif z < x and z < y:
        result = z
    return result


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))

print("O maior valor deles é: ", maior(num1, num2, num3))
print("O menor valor deles é: ", menor(num1, num2, num3))
