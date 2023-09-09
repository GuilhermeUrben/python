
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite o último número: ')))
print(f'\nVocê digitou os valores {n}')
print(f'O número \033[4m9\033[m apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número \033[4m3\033[m foi digitado na {n.index(3)+1}ª posição.')
else:
    print('O valor \033[4m3\033[m não foi digitado.')
print(f'Os números pares foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')

