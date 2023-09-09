def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except ZeroDivisionError:
            print('\033[31mERRO: Zero não é um número divisivel.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        else:
            return n


def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número Real válido.\033[m')
            continue
        except ZeroDivisionError:
            print('\033[31mERRO: Zero não é um número divisivel.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        else:
            return n


inteiro = leiaint('Digite um inteiro: ')
real = leiafloat('Digite um real: ')
print(f'Você digitou o inteiro {inteiro} e o real {real}.')
