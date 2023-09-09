# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')

if letra in 'aeiouAEIOU':
    print('Esta letra é uma vogal.')
else:
    print('Esta letra é uma consoante.')