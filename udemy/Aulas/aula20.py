# s1 = set()# vazio
# s1 = {'Guilherme', 1, 2, 3} # com dados
# s1 = {1, 2, 3, 3, 3, 3, 3, 1}
# s1 = {1, 2, 3}
# print(3 in s1)
# for numero in s1:
#     print(numero)

s1 = set()
s1.add('Guilherme')
s1.add(2)
s1.update(('Olá mundo', 1, 3, 4, 2))
# s1.clear()
s1.discard('Olá mundo')
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s2 ^ s1
print(s3)