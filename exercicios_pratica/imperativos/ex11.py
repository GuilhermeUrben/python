#  Dado um número inteiro, positivo, menor do que 1000 obter a quantidade de 
# centenas, dezenas e unidades desse número.
#  Exemplo: Dado o nº 764, obter Centena = 7, Dezena = 6 e Unidade = 4

numero = int(input("Digite um número menor que 1000, inteiro positivo: "))

# Extraindo a unidade
unidade = numero % 10

# Eliminando a unidade de nosso número
numero = (numero - unidade) / 10

# Extraindo a dezena
dezena = numero % 10

# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero

# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')
