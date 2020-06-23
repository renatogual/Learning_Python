'''As Organizações Tabajara resolveram dar um aumento de salário aos
seus colaboradores e lhe contrataram para desenvolver o programa que
calculará os reajustes. 
    Faça um programa que recebe o salário de um colaborador e o reajuste
segundo o seguinte critério, baseado no salário atual:
    -salários até R$ 280,00 (incluindo) : aumento de 20%
    -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    -salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input("Digite o salário: "))

if salario <= 280:
    percentual = 0.20
elif 280 < salario <= 700:
    percentual = 0.15
elif 700 < salario <=1500:
    percentual = 0.10
elif salario > 1500:
    percentual = 0.05
else:
    print("Valor inválido!")

print("\nSalário antes do reajuste = {}".format(salario))
print("Percentual de aumento aplicado = {}%".format(int(percentual*100)))
print("Valor do aumento = R${}".format(salario*percentual))
print("Novo salário após aumento = R${:.2f}".format(salario*(percentual+1)))

