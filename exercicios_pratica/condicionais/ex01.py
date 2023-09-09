# escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, 
# e mostre o por extenso. Este número deverá variar entre 1 e 10. Se o usuário introduzir um número que 
# não pertença a este intervalo, exiba a mensagem: “número inválido”. Exemplo: 10 ➔ Dez; 7
# ➔ Sete ; 2 ➔ Dois

numero = int(input("Digite um número inteiro positivo: "))

if numero > 0 and numero <= 10:
    if numero == 1:
        extenso = "um"
    if numero == 2:
        extenso = "dois"
    if numero == 3:
        extenso = "trez"
    if numero == 4:
        extenso = "quatro"
    if numero == 5:
        extenso = "cinco"
    if numero == 6:
        extenso = "seis"
    if numero == 7:
        extenso = "sete"
    if numero == 8:
        extenso = "oito"
    if numero == 9:
        extenso = "nove"
    if numero == 10:
        extenso = "dez"
    print(f"O número {numero}, por extenso é {extenso}.")
else:
    print("\33[31mNúmero inválido.\33[m")