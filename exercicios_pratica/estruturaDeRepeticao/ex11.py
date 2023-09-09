#  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa
# que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o seu salário: '))
reajuste = 0.0

if 280 <= salario < 700:
    aumento = salario * 0.2
    reajuste = salario + aumento
    print(f"""O seu salário é R$ {salario} reais,
você ira receber um aumento de R$ {aumento} reais 
equivalente a 20% do seu antigo salário, e seu novo salário será de R$ {reajuste} reais.""")
elif 700 <= salario < 1500:
    aumento = salario * 0.1
    reajuste = salario + aumento
    print(f"""O seu salário é R$ {salario} reais,
você ira receber um aumento de R$ {aumento} reais 
equivalente a 10% do seu antigo salário, e seu novo salário será de R$ {reajuste} reais.""")
elif salario >= 1500:
    aumento = salario * 0.05
    reajuste = salario + aumento
    print(f"""O seu salário é R$ {salario} reais,
você ira receber um aumento de R$ {aumento} reais 
equivalente a 5% do seu antigo salário, e seu novo salário será de R$ {reajuste} reais.""")
else:
    print('Error.')