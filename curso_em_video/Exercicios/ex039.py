ano = int(input('Digite o ano atual: '))
nascimento = int(input('Em que ano você nasceu? '))
idade = (ano-nascimento)
if idade == 18:
    print('Está no ano de realizar seu \033[4;32mAlistamento Militar\033[m!')
elif idade < 18:
    print('Você não tem idade suficiente para se alistar, faltam \33[4;33m{} anos\033[m para você se alistar.'.format(18-idade))
elif idade > 18:
    print('Já se passaram \33[4;31m{} anos\33[m, caso não tenha se alistado, procure sua junta militar para resolver suas pendências.'.format(idade-18))