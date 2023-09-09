def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco*taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>2.2f}'.replace('.', ',')


def linha(txt):
    print('-' * 35)
    print(f'{txt}'.center(35))
    print('-' * 35)


def resumo(preco=0, taxaa=10, taxar=5):
    linha('RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Aumento de {taxaa}%: \t{aumentar(preco, taxaa, True)}')
    print(f'Redulçao de {taxar}%: \t{diminuir(preco, taxar, True)}')
    print('_' * 35)
