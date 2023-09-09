print('Bem vindo ao Conversor de números!!! Siga as instruções abaixo.')
num = int(input('Escolha um número inteiro: '))
print('''Você deseja converter para:
1 - \33[4mBinário\33[m
2 - \33[4mOctal\33[m 
3 - \33[4mHexadecimal\33[m ''')
opção = int(input('Escolha uma das opções acima: '))
binario = 'Binário'
octal = 'Octal'
hexadecimal = 'hexadecimal'
if opção == 1:
    print('O número {} convertido para Binário é: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para Octal é: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Essa opção não existe, escolha uma das opções!')