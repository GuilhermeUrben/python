matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somat = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l},{c}]: '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f' [{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
print()
#LETRA "A"
print(f'A soma de todos os valores pares da matriz é igual a {somap}: ')
#LETRA "B"
for l in range(0, 3):
    somat += matriz[l][2]
print(f'A soma dos valores da \033[4mterceira coluna\033[m é: {somat}')
#LETRA "C"
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha foi o número {mai}')