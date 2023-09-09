def gen1():
    print('Começou GEN1')
    yield 1
    yield 2
    yield 3
    print('Acabou GEN1')


def gen3():
    print('Começou GEN3')
    yield 10
    yield 20
    yield 30
    print('Acabou GEN3')


def gen2(gen):
    print('Começou GEN2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('Acabou GEN2')


g1 = gen2(gen1)
g2 = gen2(gen3)
for n in g1:
    print(n)
for n in g2:
    print(n)
