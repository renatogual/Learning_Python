'''Faça um programa que leia 5 números e informe o maior número.'''

lista = []

for i in range(0,5):
    x = int(input("Digite um numero: "))
    lista.append(x)

print("O maior numero digitado foi: ",max(lista))



