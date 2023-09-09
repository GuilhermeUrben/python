num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = num + (10-1) * razao
for n in range(num, decimo + razao, razao):
    print(n, end=' -> ')
print('Fim')