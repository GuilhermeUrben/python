# Um palíndromo é uma sequência de caracteres que sendo lida da esquerda para a direita ou da 
# direita para a esquerda tem o mesmo valor. Por exemplo, cada um dos seguintes inteiros de 5 
# dígitos é um palíndromo: 12321, 55555, 45554 e 11611. Escreva um aplicativo que leia uma 
# sequência de números de 5 dígitos e determine se ele é ou não um palíndromo.

numeros = []

numero = input('Digite um número de 5 dígitos para saber se ele é um palíndromo: ')
numeros.append(numero)


if len(numeros[0]) == 5:
    print(f'Você digitou {numeros[0]}.')
    if numeros[0][0] == numeros[0][4] and numeros[0][1] == numeros[0][3]:
        print('Este número é um palíndromo')
    else:
        print('Este número não é um palíndromo')
else:
    print('\33[31mERROR!\33[m Digite um número com 5 dígitos.')

