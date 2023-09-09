apv = dict()
lista = list()

apv['nome'] = str(input('Nome do jogador: '))
apv['partidas'] = int(input('Partidas jogadas: '))
for g in range(0, apv['partidas']):
    gols = int(input(f'Gols marcados na {g+1}ª partida: '))
    lista.append(gols)
    apv["gols"] = lista[:]
totgols = sum(lista)
apv['total'] = totgols
print()
print(f'O jogador {apv["nome"]} jogou {apv["partidas"]} partidas e fez {apv["total"]} gols no campeonato.')
print()
for gg in range(0, apv['partidas']):
    print(f'Na {gg+1}ª partida, fez {lista[gg]} gols.')
