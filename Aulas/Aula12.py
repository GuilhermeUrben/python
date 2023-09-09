nome = str(input('Qual é o seu nome? '))
if nome == 'Gui':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='Paulo':
    print('Seu nome é bem popular!')
elif nome in 'Ana Claudia Babi Juliana':
    print('Belo nome')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))