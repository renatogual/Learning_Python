'''Faça um Programa que leia três números inteiros, em seguida mostre o
maior e o menor deles.'''

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"O maior numero digitado foi {maior} e o menor foi {menor} ")