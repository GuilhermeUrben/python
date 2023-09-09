#  Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo
# Inválido

print("""Digite seu sexo:
[M] Masculino
[F] Feminino""")

sexo = input('Sua escolha: ').strip().upper()

if sexo[0] in 'Mm':
    print('Você escolheu a opção Masculino.')
elif sexo[0] in 'Ff':
    print('Você escolheu a opção Feminino.')
else:
    print('Sexo Inválido.')