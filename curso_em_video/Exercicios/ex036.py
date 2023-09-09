financiamento = float(input('Qual o valor da sua casa? '))
salario = float(input('Qual é o seu salário? '))
prazo = int(input('Em quantos anos você pretende financiar? '))
prazomes = prazo*12
prestacao = financiamento/prazomes
cores = {'Azul' : '\033[4;32m',
         'Verde' : '\033[4;32m',
         'Vermelho' : '\033[4;31m',
         'Amarelo' : '\033[4;33m',
         'Cinza' : '\033[4;37m',
         'Branco' : '\033[4;107m'}
if prestacao < (salario*0.30):
    print('Seu Financiamento foi {}aprovado\033[m!'.format(cores['Verde']))
    print('A sua prestação será de R${:.3f},00 Reais por mês'.format(prestacao))
else:
    print('Infelizmente Seu Financiamento foi {}negado\033[m!'.format(cores['Vermelho']))
    print('A sua prestação seria de R${:.3f},00 Reais por mês'.format(prestacao))
