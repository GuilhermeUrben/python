# Faça um programa que leia a idade de uma pessoa expressa em anos, meses e dias 
# e mostre-a expressa apenas em dias, suponha todos os meses com 30 dias. 

idade = int(input("Digite sua idade: "))
idade_meses = idade * 12
idade_dias = idade * 360

print(f"""Voce tem {idade} anos de vida.
Você viveu {idade} anos.
Você viveu {idade_meses} meses.
Você viveu {idade_dias} dias.""")
