from time import sleep
contagem = int(input('Digite um tempo para contagem: '))
print('Contagem regressiva de \033[1m{} Segundos\033[m'.format(contagem))
sleep(0.5)
for c in range(contagem, -1, -1):
    print(c)
    sleep(1)
sleep(1)
print('FIM!!')