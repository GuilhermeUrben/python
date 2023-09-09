# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e
# apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if 7 <= media < 10:
    print(f'Parabéns, você foi aprovado com a média {media}.')
elif media == 10:
    print('Você foi incrível, você foi aprovado com distinção. Média 10.')
elif 0 <= media < 7:
    print(f'Você foi reprovado com a média {media}')
else:
    print('Média inválida, digite suas notas novamente.')
