lista1 = ['Salvador', 'Ubatuda', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#     ]

from itertools import zip_longest

print(list(zip(lista1, lista2)))
print()
print(list(zip_longest(lista1, lista2)))
