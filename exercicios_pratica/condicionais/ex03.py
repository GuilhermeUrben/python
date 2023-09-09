# Escreva um algoritmo que receba um número e verifique se ele é múltiplo de 3 e de 7. Escreva 
# uma das mensagens: “é múltiplo de 3 e de 7” ou “não é múltiplo de 3 e 7”.

numero = int(input('Digite um numero inteiro positivo: '))

if numero % 3 == 0 and numero % 7 == 0:
    print('Este numero é multiplo de 3 e de 7')
else:
    print('Este numero não é multiplo de 3 e de 7')
