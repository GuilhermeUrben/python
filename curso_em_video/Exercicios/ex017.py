import math

n = float(input('Digite o cateto oposto: '))
n1= float(input('Digite o cateto adjacente: '))
exp = math.exp2(n)
exp1 = math.exp2(n1)
nr = math.sqrt((exp)+(exp1))
print('O valor da hipotenusa é {}'.format(nr))