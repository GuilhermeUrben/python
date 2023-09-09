r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[0;30;107m'}
print('Os comprimentos são {}{}, {}{} e {}{}\033[m'.format(cores['azul'], r1, cores['amarelo'], r2, cores['pretoebranco'], r3))
if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print('É possivel formar o triangulo')
else:
    print('Não é possivel formar o triangulo')
