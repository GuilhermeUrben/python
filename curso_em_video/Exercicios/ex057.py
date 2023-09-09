sexo = str(input('Qual o seu sexo? [H/M] ')).strip().upper()[0]
while sexo not in 'MmHhh':
    sexo = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))