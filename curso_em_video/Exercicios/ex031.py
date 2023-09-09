distancia = float(input('Qual foi sua distância percorrida? '))
if distancia <= 200:
    print('A sua viagem custou: {} Reais'.format(distancia*0.5))
else:
    print('A sua viagem custou: {} Reais'.format(distancia*0.45))
