'''Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números ímpares.'''

lista = []
listaPar = []
listaImpar = []

for x in range(10):
    num = int(input("Digite um numero: "))
    lista.append(num)
    if lista[x] % 2 ==0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(f"Foram digitados {len(listaPar)} números pares e eles são: {sorted(listaPar)}")
print(f"Foram digitados {len(listaImpar)} números impares e eles são: {sorted(listaImpar)}")






