import emoji
import random
from time import sleep

boasvindas = print('Bem vindo ao \033[1;97mJokenpô!\033[m')
sleep(0.5)

#Tutorial de como jogar!
print('''\n\033[1;97mComo jogar\033[m: 
- Cada jogador joga 1 vez por rodada
- Na rodada você terá que escolher entre \033[4mPEDRA\033[m, \033[4mPAPEL\033[m ou \033[4mTESOURA\033[m
- Ganha quem conseguir "eliminar o adversário" 
- Caso a escolha for igual, resultará em empate''')

pedra = emoji.emojize(':fist:', language='alias')
tesoura = emoji.emojize(':v:', language='alias')
papel = emoji.emojize(':raised_hand:', language='alias')

print(
    f'''\n\033[1;97mComo eliminar\033[m:
- Pedra{pedra} quebra a Tesoura{tesoura}
- Tesoura{tesoura} corta o Papel{papel}
- Papel{papel} enrola a Pedra{pedra}
''')
sleep(1)

#Começo da rodada!
print('\n\033[1;97mComeço da rodada!!\033[m')
escolha = print('''Sua vez: 
1 - \033[4mPedra\033[m 
2 - \033[4mPapel\033[m
3 - \033[4mTesoura\033[m''')

#escolha do jogador
escolha_jogador = int(input('Qual é a sua jogada? '))
print('\nPedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura!!!')
sleep(1)
print('-' * 30)

if escolha_jogador == 1:
    print(f'Você jogou {pedra}')
elif escolha_jogador == 2:
    print(f'Você jogou {papel}')
elif escolha_jogador == 3:
    print(f'Você jogou {tesoura}')

#escolha do computador
lista = (pedra, papel, tesoura)
computador = random.choice(lista)
print(f'Computador jogou {computador}')
print('-' * 30)
if computador == pedra and escolha_jogador == 3:
    print('\033[1;31mVocê PERDEU!\033[m ')
elif computador == tesoura and escolha_jogador == 2:
    print('\033[1;31mVocê PERDEU!\033[m ')
elif computador == papel and escolha_jogador == 1:
    print('\033[1;31mVocê PERDEU!\033[m ')
elif computador == tesoura and escolha_jogador == 3:
    print('\033[1;33mEMPATE!\033[m ')
elif computador == pedra and escolha_jogador == 1:
    print('\033[1;33mEMPATE!\033[m ')
elif computador == papel and escolha_jogador == 2:
    print('\033[1;33mEMPATE!\033[m')
else:
    print('\033[1;32mVocê VENCEU! ')
