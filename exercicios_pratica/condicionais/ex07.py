# Construa um algoritmo para determinar se o indivíduo está
# com um peso favorável ou não. Essa situação é 
# determinada através do IMC ( Índice de Massa
# Corpórea), que é definida como sendo a relação entre o 
# peso (PESO) e o quadrado da Altura (ALTURA) do 
# indivíduo. A situação do peso é determinada pela fórmula:

peso = float(input('Digite seu peso (KG):  '))
altura = float(input('Digite sua altura (M): '))

imc = peso / (altura*altura)

print(f'Seu IMC é: {imc:.2f}')

if imc < 20:
    print('Você está abaixo do peso')
elif 20 <= imc < 25:
    print('Você está com peso normal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso') 
elif 30 <= imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')