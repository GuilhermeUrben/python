# Escrever um programa que leia o nome de um vendedor, o seu salário fixo e o total de 
# vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 
# 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e 
# salário no final do mês.

vendedor = input("Digite o nome do vendedor: ")
salario = float(input("Digite o salário fixo: R$ "))
vendas = int(input("Digite o valor do total de vendas efetuadas: R$ "))
comissao = vendas*0.15

print(f"""O vendendor {vendedor}, recebe um salário fixo de R${salario} reais,
com a comissão de 15% sobre as vendas de R$ {vendas}, seu salário no final do mês
ficou de R$ {salario + comissao} reais.""")