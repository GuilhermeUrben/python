'''lanche = ('Habúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu gosto de {comida} ')
print(' ')

for cont in range(0, len(lanche)):
    print(f' Eu gosto de {lanche[cont]} na posição {cont}')
print(' ')

for pos, comida in enumerate(lanche):
    print(f'Eu gosto de {comida} na posição {pos}')
print(' ')'''

'''print(sorted(lanche))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(2, 6))'''
lanche = ('Habúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f' Eu gosto de {lanche[cont]} na posição {cont}')
print(' ')

for comida in lanche:
    print(f'Eu gosto de {comida} ')
print(' ')

for pos, comida in enumerate(lanche):
    print(f'Eu gosto de {comida} na posição {pos}')
print(' ')


pessoa = ('Eu', 39, 'M', 86.3)
print(pessoa)
