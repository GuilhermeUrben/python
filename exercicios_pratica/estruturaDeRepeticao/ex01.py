# Faça um Programa que peça dois números e imprima o maior deles

maior = 0

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    maior = n1
    print(f'O maior valor entre os dois números é o {maior}.')
elif n1 == n2:
    print('Os dois valores são iguais.')
else:
    maior = n2
    print(f'O maior valor entre os dois números é o {maior}.')