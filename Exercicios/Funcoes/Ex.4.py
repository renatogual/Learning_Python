# Exercicio 4 de Funções
# A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script em Python que
# simule 1 milhão de lançamentos de dados e mostre a frequência que deu para cada número.

import random

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

for i in range(1000000):
    i += 1
    var = random.randint(1, 6)
    if var == 1:
        num1 += 1
    elif var == 2:
        num2 += 1
    elif var == 3:
        num3 += 1
    elif var == 4:
        num4 += 1
    elif var == 5:
        num5 += 1
    elif var == 6:
        num6 += 1

print("A frequencia do numero 1 é: ", num1, " vezes")
print("A frequencia do numero 2 é: ", num2, " vezes")
print("A frequencia do numero 3 é: ", num3, " vezes")
print("A frequencia do numero 4 é: ", num4, " vezes")
print("A frequencia do numero 5 é: ", num5, " vezes")
print("A frequencia do numero 6 é: ", num6, " vezes")


