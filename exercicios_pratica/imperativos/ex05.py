# Faça um programa que receba um valor que foi depositado e exiba o valor com 
# rendimento após um mês. Considere fixo o juro da poupança em 0,50% a. m.

deposito = float(input("Qual foi o valor depositado? "))
rendimento = deposito * 0.05
valor_final = deposito + rendimento

print(f"""Você depositou R$ {deposito} reais,
Em 1 mes seu rendimento foi de R$ {rendimento} reais, 
você tem um valor total de R$ {valor_final} reais.""")