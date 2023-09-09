preço = float(input('Qual o preço do produto? R$'))
print('''Qual a forma de pagamento? 
1 - dinheiro ou cheque
2 - 1x no cartão
3 - 2x no cartão
4 - 3x ou mais''')
opção = int(input('Escolha uma opção de pagamento: '))
dinheiro = preço*0.1
cartao1 = preço*0.05
cartao2 = preço/2
cartao3 = preço*0.2
if opção == 1:
    print('Você terá 10% de desconto na sua compra de R${}, com valor final de R${}'.format(preço, preço-dinheiro))
elif opção == 2:
    print('Você terá 5% de desconto na sua compra de R${}, com valor final de R${}'.format(preço, preço-cartao1))
elif opção == 3:
    print('Você pagará o preço normal do produto, com valor de R${} em 2 parcelas de R${}.'.format(preço, cartao2))
if opção == 4:
    print('Você pagará com 20% de juros na sua compra de R${}.'.format(preço))
    parcelas = int(input('Quantas parcelas? '))
    parcelado = cartao3+preço
    valorparcela = parcelado/parcelas
    print('O valor final será de R${} e com {} parcelas de R${}'.format(parcelado, parcelas, valorparcela))