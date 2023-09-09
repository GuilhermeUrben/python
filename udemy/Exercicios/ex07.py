import copy

from dados import produtos


novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

produtos_ordenadaos_por_nome = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['nome'],
)

produtos_ordenadaos_por_nome_reverse = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print('Produtos')
print(*produtos, sep='\n')
print()
print('Novos produtos')
print(*novos_produtos, sep='\n')
print()
print('Crescente')
print(*produtos_ordenadaos_por_nome, sep='\n')
print()
print('Reverso')
print(*produtos_ordenadaos_por_nome_reverse, sep='\n')

print('oba')
