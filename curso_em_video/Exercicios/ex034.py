salário = float(input('Qual o seu salário? '))
# Aumento de salário superior a R$1.250,00 é de 10%
if salário >= 1250:
    print('O seu aumento será de: {:.3f}'.format(salário*0.10))
# Aumento de salário inferior a R$1.250,00 é de 15%
if salário <= 1250:
    print('O seu aumento será de: {:.3f}'.format(salário*0.15))

