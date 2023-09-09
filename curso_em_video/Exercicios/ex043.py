print('Para calcular seu \033[4;30;IMC\033[m Siga os próximos passos.')
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
IMC = peso/(altura*altura)
print('Seu \033[4mIMC\033[m é : {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Você está \033[33mAbaixo do peso\033[m.')
elif 25> IMC >=18.5:
    print('Você está no \033[32mPeso ideal\033[m.')
elif 30> IMC >=25:
    print('Você está com \033[33mSobrepeso\033[m.')
elif 40> IMC >=30:
    print('Você está com \033[31mObesidade\033[m.')
else:
    print('Você está com \033[31mObesidade mórbida\033[m.')