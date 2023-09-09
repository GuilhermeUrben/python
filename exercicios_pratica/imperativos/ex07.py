# Faça um programa que receba o preço de custo de um produto e mostre o valor de 
# venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um 
# percentual informado pelo usuário.

custo = float(input("Digite o preço de custo do produto: "))
percentual = float(input("Digite o percentual de acréscimo você deseja colocar para esse produto: "))
venda = custo + (custo*(percentual/100))

print(f"O preço de custo do produto é de R$ {custo} reais e o valor de venda dele será de R$ {venda} reais.")