def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('\033[31mVocê não pode dividir um valor por zero.\033[m')
    return True


# def deve_ser_int_ou_float(n):


def divide(n, d):
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{d} deve ser int ou float.'
        )

    nao_aceito_zero(d)
    return n / d


print(divide(8, 0))
