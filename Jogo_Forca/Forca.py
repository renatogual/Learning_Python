# Importando a biblioteca random para escolher a palavra aleatóriamente da lista de palavras.txt
import random

# Tabuleiro
board = ['''

>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Escolhendo uma palavra aleatória do arquivo "palavras.txt"
def escolha_palavra():
    with open("palavras.txt", "r") as f:
        palavra_escolhida = f.readlines()
    return palavra_escolhida[random.randint(0, len(palavra_escolhida))].strip()

#Função que mostra o status do tabuleiro
def mostra_tabuleiro(numero):
    tabuleiro = board[numero]
    return print(tabuleiro)

#Aqui é onde a palavra escolhida é separada letra a letra
palavra = [x for x in escolha_palavra()]

#Variaveis auxiliares
lista = []
count = 0
count2 = 0
count_letra_certa = []
count_letra_errada = []

#Aqui é onde é criado o tabuleiro das letras a serem descobertos da palavra
while count < len(palavra):
    for i in palavra:
        count += 1
        lista.append("_")

#Enquanto o jogo não tiver terminado, mostra o status do tabuleiro e faz a leitura da letra
while True:
    mostra_tabuleiro(count2)
    print("Palavra: ",*lista) # O asterisco nos nomes descompactam a lista, para mostrar apenas os valores sem as aspas e virgulas
    print("Letras certas: ", *count_letra_certa)
    print("Letras erradas: ", *count_letra_errada)
    letra = str(input("Digite uma letra: "))
        
#Fazendo a leitura da letra digitada e verificando se existe na palavra ou não
    if letra in palavra:
        for i in range(0, len(palavra)):
            if palavra[i] == letra: #Caso a letra exista na palavra, verifica em qual indice ela esta para ser adicionada
                lista[i] = letra
        count_letra_certa.append(letra)
    else:
        count_letra_errada.append(letra)
        count2 += 1

#Verificando se o jogo foi vencido ou perdido
    if lista == palavra:
        print("Parabens, você venceu o jogo!")
        break
    elif count2 == 6:
        print("Game over!")
        break

        
        
