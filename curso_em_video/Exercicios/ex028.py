import random
computador = random.randint(0, 5)
n = int(input('Escolha um número entre 0 e 5: '))
if n == computador:
    print('Parabens, você acertou! ')
else:
    print('Que pena, você Errou! ')
print('O número era {}'.format(computador))