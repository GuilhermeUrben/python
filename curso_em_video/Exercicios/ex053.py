import string
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('\033[4mPalavra\033[m: ', inverso, '\033[4mInverso\033[m: ', junto)
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo! ')