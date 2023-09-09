#  Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = list()

n1 = int(input('Digite um número inteiro: '))
numeros.append(n1)
n2 = int(input('Digite outro número inteiro: '))
numeros.append(n2)
n3 = int(input('Digite outro número inteiro: '))
numeros.append(n3)
numeros.sort()

print('O números digitados em ordem crescente são:',*numeros)
