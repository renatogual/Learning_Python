''' Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo: 
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 1 '''

num = int(input("Numero menor que 1000: "))

centenas = num/100
dezenas = (num%100)/10
unidades = (num%100)%10

valida = False

if num <= 1000:
    valida = True

if valida:
    print(int(centenas),"Centenas")
    print(int(dezenas),"Dezenas")
    print(int(unidades),"Unidades")
else:
    print("Numero inválido")