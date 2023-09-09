# Escreva um algoritmo que receba o valor da idade de uma pessoa e escreva sua classificação 
# segundo a seguinte tabela abaixo:
# • maior de idade (Idade Superior ou igual a 21 Anos)
# • menor de idade (Idade Inferior a 21);
# • pessoa idosa (idade superior ou igual a 65 anos).

idade = int(input('Digite sua idade: '))

if 21 <= idade < 65:
    print(f'Você tem {idade} anos e é maior de idade.')
elif idade >= 65:
    print(f'Você tem {idade} e é uma pessoa idosa.')
else:
    print(f'Você tem {idade} anos e é menor de idade.')