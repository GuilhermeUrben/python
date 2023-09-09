lista = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1º nota do aluno: '))
    nota2 = float(input('Digite a 2º nota do aluno: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    r = str(input('Você quer continuar? [S/N]: '))
    while r not in 'SsNn':
        r = str(input('Você quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print('_'*38)
print(f'{"Nº":<10}{"Nome":<10}{"Média":>10}')
print('_'*38)
for i, a in enumerate(lista):
    print(f'{i:<10} {a[0]:<10} {a[2]:>7.1f}')
while True:
    r2 = int(input('Você quer saber as notas de algum aluno? [999 para sair] digite o número dele: '))
    if r2 == 999:
        print('FIM DO PROGRAMA.')
        break
    if r2 <= len(lista) - 1:
        print(f'As notas de {lista[r2][0]} são {lista[r2][1]}')
print('_'*38)
