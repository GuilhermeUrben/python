maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Qual é o preso da {}ª pessoa (KG): '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa com o maior peso tem {} KG'.format(maior))
print('A pessoa com o menor peso tem {} KG'.format(menor))
