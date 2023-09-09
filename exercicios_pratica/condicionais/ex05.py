#                                                                       SALDO MÉDIO   |        PERCENTUAL
# A CEF concederá um crédito especial                                  de 0 a 500     |   Nenhum critério
# com juros de 2% aos seus clientes de                                 de 501 a 1000  |   30% do valor do saldo médio
# acordo com o saldo médio no último ano.                              de 1001 a 3000 |   40% do valor do saldo médio
# Fazer um algoritmo que leia o saldo                                  Acima de 3001  |   50% do valor do saldo médio
# médio de um cliente e calcule o valor do 
# crédito de acordo com a tabela a seguir. 
# Escreva uma mensagem informando o 
# saldo médio e o valor de crédit

saldoMedio = float(input('Qual o seu saldo médio: '))

credito = 0.0

if 0 <= saldoMedio <= 500:
    print(f'O seu saldo médio é de R$ {saldoMedio} e você não tem direito a crédito')
elif 501 <= saldoMedio <= 1000:
    credito = saldoMedio * 0.3
    print(f'O seu saldo médio é de R$ {saldoMedio} e o valor do seu crédito é de {credito}')
elif 1001 <= saldoMedio <= 3000:
    credito = saldoMedio * 0.4
    print(f'O seu saldo médio é de R$ {saldoMedio} e o valor do seu crédito é de {credito}')
elif saldoMedio >= 3001:
    credito = saldoMedio * 0.5
    print(f'O seu saldo médio é de R$ {saldoMedio} e o valor do seu crédito é de {credito}')
else:
    print('Error.')