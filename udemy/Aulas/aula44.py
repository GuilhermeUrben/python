from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camiseta = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino'],
    ['algodão', 'dryfit'],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camiseta))
