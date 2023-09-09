def produto(*args):
    produto = 1
    for numero in args:
        produto *= numero
    print(f'O valor da multiplicação foi "{produto}" ', end='')
    if produto % 2 == 0: 
        print('e ele é PAR.')
    else:
        print('e ele é IMPAR.')
    return


mult = produto(3, 3, 10)