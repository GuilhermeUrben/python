def leiaDinheiro(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERROR: \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)
