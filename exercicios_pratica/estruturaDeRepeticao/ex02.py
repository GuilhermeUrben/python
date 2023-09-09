# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input('Digite um valor inteiro: '))

if valor < 0:
    print('Este valor é negativo.')
elif valor > 0:
    print('Este valor é positivo.')
else:
    print('esse valor é neutro.')