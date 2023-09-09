# Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:
# • não eleitor (abaixo de 16 anos);
# • eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
# • eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)

idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Você não é um eleitor.')
elif 16 <= idade < 18 or idade >= 65:
    print('Você é um eleitor facultativo.')
else:
    print('Você é um eleitor obrigatório.')