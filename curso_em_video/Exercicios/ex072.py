#Cores
Azul = '\033[1;34m'
Vermelho = '\033[1;31m'
Amarelo = '\033[1;33m'
Verde = '\033[1;32m'
Branco = '\033[1;97m'
sublinhado = '\033[4m'
finalcor = '\033[m'


numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
          'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
          'Quinte', 'Dezesseis', 'Dezessete', 'Dezoito',  'Dezenove', 'Vinte')
for num in range(1, len(numero)):
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 21:
        print(f'{Verde}O número {sublinhado}{num}{finalcor} {Verde}por extenso é:  {numero[num]}{finalcor}')
    else:
        print(f'{Vermelho}Tente novamente, digite um número entre 0 e 20.{finalcor} ')