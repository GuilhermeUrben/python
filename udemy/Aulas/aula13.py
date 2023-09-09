# cpf = '602.186.820-00'

# #REMOVER O HIFEN DO CPF.
# remover_hifen = cpf.split('-')
# cpf_sem_hifen = remover_hifen[0]

# for num in remover_hifen:
#     remover_hifen.pop()

# #REMOVER O PONTO DO CPF.
# remover_ponto = cpf_sem_hifen.split('.')
# cpf_sem_ponto = remover_ponto

# #SOMA DOS VALORES DA LISTA PARA TER UM CPF "LIMPO".
# cpf = cpf_sem_ponto[0] + cpf_sem_ponto[1] + cpf_sem_ponto[2]

#OBTENDO O PRIMEIRO DIGITO.
cpf_enviado = '559.444.450-50' \
.replace('.', '') \
.replace(' ', '') \
.replace('-', '')

nove_digitos = cpf_enviado[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

#OBTENDO O SEGUNDO DIGITO.
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

#CPF GERADO COM OS 2 ULTIMOS DIGITOS.
cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

#ANALISANDO SE O CPF É VALIDO
if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF inválido')