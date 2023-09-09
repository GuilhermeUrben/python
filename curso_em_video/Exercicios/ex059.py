from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print(' ')
escolha = 0
while escolha != 5:
    sleep(1)
    print('''Você pode escolher entre as 5 opções abaixo:
    1 - SOMAR
    2 - MULTIPLICAR
    3 - MAIOR
    4 - NOVOS NÚMEROS
    5 - SAIR DO PROGRAMA''')
    escolha = int(input('Qual opção voce quer escolher? '))
    print(' ')
    sleep (1)
    if escolha == 1:
        soma = n1 + n2
        print('A soma dos dois valores é igual a {}.'.format(soma))
    elif escolha == 2:
        mult = n1*n2
        print('A multiplicação dos dois valores é igual a {}'.format(mult))
    elif escolha == 3:
        if n1 > n2:
            print('O número {} é maior.'.format(n1))
        elif n1 < n2:
            print('O número {} é menor'.format(n1))
    elif escolha == 4:
        n3 = int(input('Digite um novo valor para subistituir {}: '.format(n1)))
        n4 = int(input('Digite um novo valor para subistituir {}: '.format(n2)))
    elif escolha == 5:
        sleep(0.3)
        print('Finalizando...')
    else:
        print('Oplção inválida. Tente novamente')
    print('''_'''*40)
    print(' ')
print('Fim do programa! Volte sempre')