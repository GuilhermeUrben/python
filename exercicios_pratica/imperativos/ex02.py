# Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que
# a variável A passe a possuir o valor da variável B e a variável B passe a possuir o
# valor da variável A. Apresentar os valores trocados.

a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

# n é uma variavel auxiliar, que recebe o valor de "a"
n = a

# a recebe o valor de "b"
a = b

# "b" recebe o valor de "n" (variavel) que recebeu valor de "a" inicialmente.
b = n

print(f"\nO valor de A é {a}")
print(f"O valor de B é {b}")
