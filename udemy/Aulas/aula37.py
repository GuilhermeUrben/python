try:
    print('Abrir Arquivo')
    # 9/0
except ZeroDivisionError:
    print('ERROR: Dividiu ZERO')
finally:
    print('Fechar arquivo')
