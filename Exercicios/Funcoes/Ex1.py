# Exercicio 1 de Funções
# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau
# Celsius para Farenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o
# usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

def fahrenheit():
    x = float(input("Digite o numero que será convertido de Graus Celcius para Fahrenheit: "))
    return (x * 1.8) + 32


def celcius():
    x = float(input("Digite o numero que será convertido de Fahrenheit para Graus Celcius: "))
    return (x - 32) / 1.8


def menu():
    while True:
        escolha = int(input("Qual conversão deseja fazer? (1) Celcius em Fahrenheit (2) Fahrenheit em Celcius: "))
        if escolha == 1:
            a = fahrenheit()
            print("O resultado é: ", a)
        elif escolha == 2:
            b = celcius()
            print("O resultado é: ", b)
        else:
            print("Opção incorreta, digite novamente: ")

menu()
