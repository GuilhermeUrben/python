lista = [[], []]
n = 0

for c in range(0, 7):
    n = (int(input(f'Digite o {1+c}º número: ')))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n)
print(f'Os valores pares foram {lista[0]}')
print(f'Os valores ímpares foram {lista[1]}')