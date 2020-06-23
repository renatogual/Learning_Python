'''Altere o programa anterior permitindo ao usuário informar as populações e
as taxas de crescimento iniciais. Valide a entrada e permita repetir a
operação.'''

while True:
    populacaoA = int(input("Digite o valor da população do país A: "))
    populacaoB = int(input("Digite o valor da população do país B: "))

    txA = float(input("Digite a tx de crescimento anual do país A: "))
    txB = float(input("Digite a tx de crescimento anual do país B: "))


    anos = 0

    while (populacaoA < populacaoB):
        anos += 1
        populacaoA += populacaoA*((txA/100)+1)
        populacaoB += populacaoB*((txB/100)+1)

    print(f"Levou {anos} anos para a população do país A ultrapassar a do país B")

    escolha = str(input("Deseja repetir a operação? [s/n]: "))
    if escolha == "n":
        break
    else:
        continue
