'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
salario = float(input("Digite o salário de seu colaborador:"))

if salario <= 280.0:
    print("O salário antes do reajuste era de:", salario)
    print("O percentual de aumento foi de: 20/100")
    valoraumento = salario *20 /100
    print("O valor do aumento foi de:", valoraumento)
    novoSalario = salario + valoraumento
    print("O novo salário será de:", novoSalario)
    
elif salario > 280.0 and salario <= 700.0:
    print("O salário antes do reajuste era de:", salario)
    print("O percentual de aumento foi de: 15/100")
    valoraumento = salario *15 /100
    print("O valor do aumento foi de:", valoraumento)
    novoSalario = salario + valoraumento
    print("O novo salário será de:", novoSalario)

elif salario > 700.0 and salario <= 1500.0:
    print("O salário antes do reajuste era de:", salario)
    print("O aumento será de:", salario * 10 /100)
    print("O percentual de aumento foi de: 10/100")
    valoraumento = salario *10 /100
    print("O valor do aumento foi de:", valoraumento)
    novoSalario = salario + valoraumento
    print("O novo salário será de:", novoSalario)

elif salario > 1500.0:
    print("O salário antes do reajuste era de:", salario)
    print("O aumento será de:", salario * 5 /100)
    print("O percentual de aumento foi de: 5/100")
    valoraumento = salario *5 /100
    print("O valor do aumento foi de:", valoraumento)
    novoSalario = salario + valoraumento
    print("O novo salário será de:", novoSalario)