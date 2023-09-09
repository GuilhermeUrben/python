# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = 0

if n1 > n2 and n1 > n3:
    maior = n1
    print(f'O maior valor é o número {maior}.')
elif n2 > n3 and n2 > n1:
    maior = n2
    print(f'O maior valor é o número {maior}.')
else:
    maior = n3
    print(f'O maior valor é o número {maior}.')