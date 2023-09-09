"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        print(f'O número {n} é \033[32mPAR\033[m.')
    else:
        print(f'O número {n} é \033[32mIMPAR\033[m.')
except:
    print('Esse número não é um INTEIRO.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""