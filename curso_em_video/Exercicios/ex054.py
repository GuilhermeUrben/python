from datetime import date
anoa = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    ano = int(input('Qual ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = anoa - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Tivemos \033[4m{}\033[m pessoas maiores de idade'.format(totmaior))
print('Tivemos \033[4m{}\033[m pessoas menores de idade'.format(totmenor))