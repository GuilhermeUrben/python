print('Escolha dois numeros inteiros: ')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O primeiro valor é \033[1;34m Maior')
elif num1 < num2:
    print('O segundo valor é \033[1;34m Maior')
elif num1 == num2:
    print('Não existe valor maior, os dois são \033[1;34m Iguais')