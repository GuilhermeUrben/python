lista = []
while True:
    n = int(input('Digite um número: '))
    resp = str(input('Você quer continuar? [S/N]: '))
    lista.append(n)
    while resp not in 'SsNn':
        print('Responda entre [S ou N]. ')
        resp = str(input('Você quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('')
print(f'A lista digitada foi {lista}')
#LETRA "A"
print(f'Foram digitados {len(lista)} números.')
#LETRA "B"
lista.sort(reverse=True)
print(f'A lista de números em forma ordenada de forma decrescente foi {lista}.')
#LETRA "C"
if 5 in lista:
    print('O valor 5 foi digitado, e está na lista.')
else:
    print('O valor 5 não foi digitado, e não está na lista.')