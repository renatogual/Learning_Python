'''Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida.'''

print("Digite uma data no formato dd/mm/aaaa")

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

valida = False

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or  
    mes == 10 or mes == 12): #Meses com 31 dias
    if (dia <=31):
        valida = True
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11): #Meses com 30 dias
    if (dia <=30):
        valida = True
elif (mes == 2):
    if (ano%4 == 0 and ano%400 != 0) or (ano%400 == 0): #Testando se ano é bissexto
        if (dia <= 29):
            valida = True
    elif (dia <= 28):
        valida = True

if valida:
    print("Data válida")
else:
    print("Data inválida!")






