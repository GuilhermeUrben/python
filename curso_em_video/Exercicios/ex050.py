soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont +=1
print('A soma dos {} números pares é: {}'.format(cont, soma))