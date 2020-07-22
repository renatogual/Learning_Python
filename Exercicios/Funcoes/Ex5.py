'''A série de Fibonacci é uma sequência de números, cujos dois primeiros
são 0 e 1. O termo seguinte da sequência é obtido somando os dois
anteriores. Faça uma script em Python que solicite um inteiro positivo ao
usuário, n. Então uma função exibe todos os termos da sequência até o n-
ésimo termo. Use recursividade.'''

def Fibonacci(x):
    penultimo = 1
    ultimo = 1
    lista = [penultimo, ultimo]
    if (x==1) or (x==2):
        return 1
    else:
        count = 3
        while count <= x:
            termo = penultimo + ultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            lista.append(termo)
    
    return lista

n = int(input("Digite um numero inteiro: "))
print(Fibonacci(n))