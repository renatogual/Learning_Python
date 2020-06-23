'''Faça um programa que pede dois numeros inteiros e armazene em duas variáveis.
Em seguida, troque o valor das variáveis e exiba na tela'''

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

print("\nVariavel 1: ",num1)
print("Variavel 2: ",num2)

aux = num2
num2 = num1
num1 = aux

print("\nApós inversão:")
print("Variavel 1: ",num1)
print("Variavel 2: ",num2)


