# Elaborar um programa que efetue a apresentação do valor da conversão em real (R$) 
# de um valor lido em dólar (US$). O programa deverá solicitar o valor da cotação do 
# dólar e a quantidade de dólares disponíveis com o usuário.

print("Conversão de dólar para real")
dolar = float(input("\nQuantos dolares você tem: "))
cotacao = float(input("Qual a cotação do dólar hoje? "))

real = dolar * cotacao

print(f"\nA cotacao do dolar está em R$ {cotacao:.2f}, você tem $ {dolar:.2f} dolares que equivalem R$ {real:.2f} reais.")
1