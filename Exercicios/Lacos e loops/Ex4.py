'''Supondo que a população de um país A seja da ordem de 80000
habitantes com uma taxa anual de crescimento de 3% e que a população de
B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.'''

populacaoA = 80000
populacaoB = 200000

txA = 1.03
txB = 1.015

anos = 0

while (populacaoA < populacaoB):
    anos += 1
    populacaoA += populacaoA*txA
    populacaoB += populacaoB*txB

print(f"Levou {anos} anos para a população do país A ultrapassar a do país B")

