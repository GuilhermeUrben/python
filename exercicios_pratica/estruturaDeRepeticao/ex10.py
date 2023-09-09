# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a
# mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

turno = input("""Qual turno você estuda?

[M] Manhã
[V] Vespertino
[N] Noturno

Sua escolha: """)

if turno in 'Mm' or turno == "manha":
    print('Bom dia')
elif turno in 'Vv' or turno == "vespertino":
    print('Boa tarde')
elif turno in 'Nn' or turno == "noturno":
    print('Boa noite')    
else:
    print('Turno Inválido')