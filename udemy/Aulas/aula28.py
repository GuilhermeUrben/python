produto = {
    'nome': 'Caneta Azul',
    'preço': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = [ 
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

dc = {
    chave: valor 
    for chave, valor in lista
}

s1 = {i ** 2 for i in range(10)}
print(s1)
