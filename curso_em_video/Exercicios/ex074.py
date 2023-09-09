import random
numero = random.randint(1, 20), random.randint(1,20), random.randint(1,20), random.randint(1, 20), random.randint(1,20)
print(' ')
print(f'Os números sorteados foram: ', end='')
for n in numero:
    print(f'{n} ', end='')
print(' ')
print(f'O maior número sorteado foi o {max(numero)}')
print(f'O menor número sorteado foi o {min(numero)}')