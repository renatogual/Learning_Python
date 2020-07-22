# Ex.25 Python Progressivo
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

turma = int(input("Digite quantas pessoas há na turma: "))
soma = 0
media = 0

for count in range(turma):
    count += 1
    idade = int(input("Digite a idade do aluno %.d: " % count))
    soma += idade
    media = soma / turma

if 0 < media <= 25:
    print("A turma é jovem")
elif 25 < media <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")
