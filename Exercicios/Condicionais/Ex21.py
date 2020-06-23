'''21. Faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma
classificação sobre a participação da pessoa no crime. Se a pessoa
responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
contrário, ele será classificado como "Inocente".'''

print("Digite 1 para 'sim' e 0 para 'não'.")
qt1 = int(input("Telefonou para a vitima? "))
qt2 = int(input("Esteve no local do crime? "))
qt3 = int(input("Mora perto da vítima? "))
qt4 = int(input("Devia para a vítima? "))
qt5 = int(input("Já trabalhou com a vítima? "))

if (qt1+qt2+qt3+qt4+qt5) == 2:
    print("Suspeito")
elif 3 <= (qt1+qt2+qt3+qt4+qt5) <= 4:
    print("Cúmplice")
elif (qt1+qt2+qt3+qt4+qt5) == 5:
    print("Assassino")
else:
    print("Inocente")
 
