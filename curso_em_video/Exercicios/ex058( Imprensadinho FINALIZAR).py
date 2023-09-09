from time import sleep
from random import randint

Computador = randint(0, 10)
Palpites = 0

#BEM VINDOS
print('\033[1mBem vindo ao jogo Imprensadinho!!!! \033[m ')
sleep(1)
print(' ')

#COMO JOGAR
print('''\033[1mComo jogar:\033[m
O jogo se baseia em acertar o número escolhido pelo \033[4mComputador\033[m
- Pirmeiro o computador escolhe um número aleatório entre 0 e 100
- E em seguida você tem que tentar imprensar o computador com os números
- Ganha se você conseguir imprensar o número que o computador escolheu, sem falar o mesmo.
- EX: Número sorteado \033[4m52\033[m, você ganhará caso consiga dizer os números \033[4m51 e 53\033[m, sem escolher o numero \033[4m52\033[m.''')
print(' ')
sleep(2)

#COMO IMPRENSAR
print('''\033[1mComo imprensar:\033[m
- O jogador vai ter que falar um número, caso o número não seja o que o computador escolheu, o computador dará uma dica.
Ex: O número sorteado é \033[4m52\033[m, e o jogador escolheu o número \033[4m30\033[m, o computador terá que falar que o número está entre \033[4m30 e 100\033[m,
caso o jogador escolha em seguida o número \033[4m60\033[m, o computador terá que falar que o número está entre \033[4m30 e 60\033[m, até que o jogador erre ou imprense o Computador.''')
print(' ')
sleep(3)

#COMEÇO DO JOGO
print('\033[1mComeço do jogo:\033[m ')
sleep(1)
Acertou = False
while not Acertou:
    jogador = int(input('Tente adivinhar o número entre 0 e 100 que o computador escolheu: '))
    for jogador in range():
        print('O número está entre \033[4m{}\033[m e \033[4m{}\033[m'.format(jogador, Computador))
    Palpites += 1
    if jogador == Computador:
        Acertou = True
print('Você acertou, o número escondido era {}'.format(Computador))







"""n = int(input('Escolha um número entre 0 e 5: '))
if n >= 3:
    print('Parabens, você acertou! ')
else:
    print('Que pena, você Errou! ')
    
    
    
    from time import sleep
from random import randint

print('\033[1mComeço do jogo, adivinhe o número do computador entre 0 e 10:\033[m ')
sleep(1)
Acertou = False
Computador = randint(0, 10)
Palpites = 0
while not Acertou:
    jogador = int(input('Digite um número: '))
    Palpites += 1
    if jogador == Computador:
        Acertou = True
    else:
        if Computador < jogador:
            print('O número está entre \033[4m{}\033[m e \033[4m{}\033[m: '.format(0, jogador))
        elif Computador > jogador:
            print('O número está entre \033[4m{}\033[m e \033[4m{}\033[m'.format(jogador, 10))
print('Você acertou, o número escondido era {} e você tentou {} vezes.'.format(Computador, Palpites))"""
