'''Faça um Programa que leia três números e mostre-os em ordem
decrescente.'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

maior = num1
meio = num1
menor = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3
    if num2 > num1: 
        meio = num2

if num2 < menor:
    menor = num2
    if num3 < menor:
        menor = num3
        meio = num2

print("Ordem decrescente: {0} {1} {2}".format(maior,meio,menor))

