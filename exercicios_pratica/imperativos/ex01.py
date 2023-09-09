# Faça um programa que receba dois números e ao final mostre a soma, subtração,
# multiplicação e a divisão dos números lidos.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print(f"\nA soma de {n1} + {n2} é igual a \33[1;32m{soma}\33[m.")
print(f"A subtração de {n1} - {n2} é igual a \33[1;32m{subtracao}\33[m.")
print(f"A multiplicação de {n1} x {n2} é igual a \33[1;32m{multiplicacao}\33[m.")
print(f"A divisão de {n1} / {n2} é igual a \33[1;32m{divisao}\33[m.")
