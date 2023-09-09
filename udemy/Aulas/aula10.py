lista = list()

print('''O que voce deseja fazer:
A - Inserir
B - Apagar
C - Listar
D - Sair''')

print()
#PROGRAMA PRINCIPAL
while True:
    resp = str(input('Selecione uma opção: '))
    if resp in '':
        print('Digite uma das opções.')
        continue
#INSERIR UM VALOR A LISTA
    elif resp in 'Aa':
        add = input('Valor: ')
        lista.append(add)
#APAGAR UM INDICE DA LISTA
    elif resp in 'Bb':
        remover = input('O que você quer remover da lista? ')
        try:
            indice = int(remover)
            del lista[indice-1]
        except ValueError:
            print('\033[31mERRO: Digite um valor inteiro.\033[m')
        except IndexError:
            print('\033[31mERRO: Índice não existe na lista. Digite um indice válido.\033[m')
#MOSTRAR A LISTA
    elif resp in 'Cc':
        for i, v in enumerate(lista):
            print(i+1, v)
#SAIR DO PROGRAMA
    elif resp in 'Dd':
        print('Finalizando...')
        break    
    else:
        print('Escolha uma das opções "A, B, C ou D"')
print('Fim do programa.')