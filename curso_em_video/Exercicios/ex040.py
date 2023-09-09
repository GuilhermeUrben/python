n1 = float(input('Qual foi a nota da 1ª prova? '))
n2 = float(input('Qual foi a nota da 2ª prova? '))
média = (n1+n2)/2
cores = {'Azul' : '\033[4;34m',
         'Vermelho' : '\033[4;31m',
         'Verde' : '\033[4;32m',
         'Amarelo' : '\033[4;33m'}
if média < 5.0:
    print('Você foi {}REPROVADO\033[m, Sua média foi \033[4m{:.2f}.\033[m'.format(cores['Vermelho'], média))
elif média >= 7.0:
    print('Parabéns!! Você foi {}APROVADO\033[m, Sua média foi \033[4m{:.2f}.\033[m'.format(cores['Verde'], média))
else:
    print('Você está na {}RECUPERAÇÃO\033[m, Sua média foi \033[4m{:.2f}.\033[m'.format(cores['Amarelo'], média))
