# def dobro(num):
#     return num * 2

# num = dobro(int(input('Digite um valor para duplicar: ')))
# print(num)

# def triplo(num):
#     return num * 3

# num = triplo(int(input('Digite um valor para triplicar: ')))
# print(num)

# def quadruplo(num):
#     return num * 4

# num = quadruplo(int(input('Digite um valor para quadruplicar: ')))
# print(num)

def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)

print(duplicar(7))