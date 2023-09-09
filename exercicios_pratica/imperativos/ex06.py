# A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem 
# juros. Faça um programa que receba um valor de uma compra e mostre o valor das 
# prestações.

compra = float(input("Digite o valor da sua compra: R$  "))

for i in range(0, 5):
    prestacao = (compra / (i+1))
    if i+1 > 1:
        print(f"O valor parcelado em {i+1} vezes, ficará R$ {prestacao:.2f} reais, por mes.")
    else:
        print(f"O valor parcelado em {i+1} vez, ficará R$ {prestacao:.2f} reais.")
