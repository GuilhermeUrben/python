# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre
# pelo mais barato

p1 = float(input('Digite o preço do primeiro produto: '))
p2 = float(input('Digite o preço do segundo produto: '))
p3 = float(input('Digite o preço do terceiro produto: '))

menor = 0.0

if p1 < p2 < p3:
    menor = p1
    print(f'O produto que você deve comprar é o primerio produto, com valor de {p1}.')
if p2 < p1 < p3:
    menor = p2
    print(f'O produto que você deve comprar é o segundo produto, com valor de {p2}.')
else:
    menor = p3
    print(f'O produto que você deve comprar é o terceiro produto, com valor de {p3}.')
