""" Crie uma função que recebe um inteiro positivo e teste para saber se ele é
primo ou não. Faça um script que recebe um inteiro n e mostra todos os
primos, de 1 até n. """

def Primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def Exibe():
    n = int(input("Exibir primos até o numero: "))
    for i in range(2, n+1):
        if (Primo(i)):
            print(i)

while True:
    Exibe()