velho = 0
mediai = 0
somai = 0
somamenor = 0
nomevelho = ''
for pessoas in range(1,5):
    print('\033[1m--- {}ª PESSOA ---\033[m '.format(pessoas))
    nome = str(input('Qual o nome? ')).strip()
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual é o sexo? ')).strip()
    somai += idade
    mediai = somai / 4
    if pessoas == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        somamenor += 1
print('A media de idade é de \033[1m{} anos\033[m.'.format(mediai))
print('O homem mais velho tem 3\03[1m{} anos\033[m e se chama \033[4m{}\033[m.'.format(velho ,nomevelho))
print('Ao todo são \033[1m{} Mulheres\033[m com menos de 20 anos.'.format(somamenor))