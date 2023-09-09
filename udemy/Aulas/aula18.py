# pessoa = {
#     'nome': 'Guilherme',
#     'sobrenome': 'Urben',
#     'idade': 27
# }

# print(pessoa['nome'])
# pessoa.setdefault('idade', 20)
# print(pessoa['idade'])

d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1.copy()

d2['oi'] = 20
print(d1)
print(d2)