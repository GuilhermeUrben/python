numeros = list()
maior = 0
menor = 0

for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print('_'*60)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor foi o {maior} e foi digitado na posição ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{v},', end=' ')
print(f'\nO menor valor foi o {menor} e foi digitado na posição ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{v},', end='')
print()
print('_'*60)