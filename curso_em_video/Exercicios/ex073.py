times = ('Palmeiras', 'Internacional', 'Fluminense', 'Cotinthias', 'Flamengo', 'Athletico-PR',
         'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goias',
         'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(' ')
print(f'Os 5 primeiros times são {times[0:5]}')
print(' ')
print(f'Os 4 últimos times são {times[-4:]}')
print(' ')
print(sorted(times))
print(' ')
print(f'O Avaí está em {times.index("Avaí")+1}ª posição.')