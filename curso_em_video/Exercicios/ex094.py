pessoas = dict()
lista = list()
mulheres = list()
maior = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [H/M]: ')).strip().upper()
        if pessoas['sexo'] in 'Mm':
            mulheres.append(pessoas['nome'])
        if pessoas['sexo'] in 'HhMm':
            break
        print('Digite H ou M.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    media = soma / len(lista)
    if pessoas['idade'] > media:
        maior.append(pessoas['nome'])
    while True:
        r = str(input('Você quer continuar [S/N]? ')).strip().upper()
        if r in 'SsNn':
            break
        print('Digite Sim ou Não.')
    if r in 'Nn':
        break
print(f'{len(lista)} pessoas foram cadastradas, dentre elas {len(mulheres)} mulheres.')
print(f'A média de idade é de {media:.2f} anos.')
print(f'As {len(mulheres)} mulheres cadastradas foram: {mulheres}')
if maior == 1:
    print(f'A pessoa com idade acima da média, foi {maior}')
else:
    print(f'As pessoas com idade acima da média, foram {maior}')


