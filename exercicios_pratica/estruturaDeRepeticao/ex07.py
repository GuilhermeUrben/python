#   Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = 0
menor = 0

if n1 > n2 and n1 > n3 and n2 < n3:
    maior = n1
    menor = n2
    print(f'O maior valor é o número {maior}.')
    print(f'O menor valor é o número {menor}.')
elif n2 > n3 and n2 > n1 and n3 < n2:
    maior = n2
    menor = n3
    print(f'O maior valor é o número {maior}.')
    print(f'O menor valor é o número {menor}.')
else:
    maior = n3
    menor = n1
    print(f'O maior valor é o número {maior}.')
    print(f'O menor valor é o número {menor}.')