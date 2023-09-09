galera = list()
dado = list()
pes = lev = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        pes = lev = dado[1]
    else:
        if dado[1] > pes:
            pes = dado[1]
        if dado[1] < lev:
            lev = dado[1]
    r = str(input('Você quer continuar? [S/N]: '))
    galera.append(dado[:])
    dado.clear()
    while r not in 'SsNn':
        r = str(input('Você quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print()
print(galera)
print(f'{len(galera)} pessoas foram cadastradas.')
print(f'O maior peso foi de {pes} KG. Peso de ', end='')
for p in galera:
    if p[1] == pes:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {lev} KG. Peso de ', end='')
for p in galera:
    if p[1] == lev:
        print(f'[{p[0]}] ', end='')
