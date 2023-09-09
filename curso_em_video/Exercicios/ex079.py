numeros = list()

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado.')
        resp = str(input('Quer continuar? [S/N]: '))
        while resp not in 'SsNn':
            print('Resposta inválida, digite [S ou N]')
            resp = str(input('Quer continuar? [S/N]: '))
        if resp in 'Nn':
            break
    else:
        print('Este número já foi adicionado. Digite Outro número')
numeros.sort()
print()
print(f'Os números adicionados foram {numeros}')