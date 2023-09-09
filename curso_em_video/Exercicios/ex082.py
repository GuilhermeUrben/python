lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Você quer continuar? [S/N]: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    while r not in 'SsNn':
        print('Digite uma resposta entre [S ou N].')
        r = str(input('Você quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print('')
#LISTA
print(f'Os valores digitados foram {lista}.')
#LISTA PAR
print(f'Os valores "Pares" digitados na lista foram: {listapar}.')
# LISTA IMPAR
print(f'Os valores "Impares" digitados na lista foram: {listaimpar}')