produtos = ('Caneta', 1.50,
            'Lápis', 1.25,
            'Borracha', 2.00,
            'Corretivo', 3.00,
            'Livro', 50.00,
            'Caderno', 15.00,
            'Bolsa', 75.00)
print('\033[1m-\033[m'*40)
print(f'\033[1m{"Tabela de preços dos prodrutos":^40}\033[m')
print('\033[1m-\033[m'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')