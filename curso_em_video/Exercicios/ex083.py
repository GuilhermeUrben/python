exp = str(input('Digite uma expressão qualquer: '))
lista = []
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão não está válida.')
