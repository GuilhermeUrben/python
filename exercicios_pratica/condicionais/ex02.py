# Escreva um algoritmo que receba um valor numérico de 3(três) dígitos e exiba a soma dos 
# algarismos que compõe este número. Exemplo: 145 -> 1+4+5 = 10

numero = int(input('numero: '))
escolha = numero

if numero > 0:
    soma = 0
    while numero != 0:
        resto = numero % 10
        numero = (numero - resto) // 10
        soma = soma + resto
    print(f'O seu número foi {escolha} e a soma dos 3 digitos é: {soma}')
else:
    print('numero invalido...')
    print('')
    