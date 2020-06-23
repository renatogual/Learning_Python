'''Faça um programa que leia 5 números e informe a soma e a média dos
números.'''

lista = []
soma = 0

for i in range(0,5):
    x = int(input("Digite um numero: "))
    lista.append(x)
    soma += lista[i]

print(f"A soma é: {soma}")
print(f"A média é: {soma/5}")

