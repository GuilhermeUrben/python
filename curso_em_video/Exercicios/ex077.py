negrito = '\033[1m'
finalnegrito = '\033[m'
sublinhado = '\033[4m'
verde = '\033[32m'

palavras = ('Estudar', 'Programar', 'Phyton', 'Computador', 'Aprender', 'Sentar', 'leitura', 'Pesquisar', 'Tentar')
for p in palavras:
    print('\nNa palavra', f'{negrito}{p.upper()}{finalnegrito}', 'temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{sublinhado}{verde}{letra.upper()}{finalnegrito}', end=' ')