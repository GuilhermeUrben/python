velocidade = float(input('Qual velocidade você estava dirigindo? '))
multa = (velocidade-60)*7
if velocidade > 60:
    print('Você ultrapassou o limite de velocidade, e foi multado no valor de R${} Reais'.format(multa))
else:
    print('Você respeitou o limite de velocidade, Parabéns! ')
