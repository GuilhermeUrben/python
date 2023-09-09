frase =  'Olha só que, coisa interessante            '
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()

print(lista_frases)