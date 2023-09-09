a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
# Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor numero é {}'.format(menor))
# Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior numero é {}'.format(maior))