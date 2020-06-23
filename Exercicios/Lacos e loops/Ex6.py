'''Faça um programa que imprima na tela os números de 1 a 20, um abaixo
do outro. Depois modifique o programa para que ele mostre os números um
ao lado do outro.'''

escolha = int(input("Digite 1 para imprimir os numeros na vertical ou 2 para horizontal: "))

if escolha == 1:
    for i in range(0,21):
        print(i)
elif escolha == 2:
    print(*range(0,21))
else:
    print("Valor inválido")
