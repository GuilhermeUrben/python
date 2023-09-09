num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divísivel {} vezes'.format(num, tot))
if tot == 2:
    print('O número {} é PRIMO '.format(num))
else:
    print('O número {} NÃO É PRIMO'.format(num))