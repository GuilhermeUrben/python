aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
print(aluno)
if aluno['media'] >= 7:
    aluno["situação"] = 'APROVADO'
    print(f'O {aluno["nome"]} teve média {aluno["media"]} e foi {aluno["situação"]}.')
elif 5 <= aluno['media'] < 7:
    aluno["situação"] = 'RECUPERAÇÃO'
    print(f'O {aluno["nome"]} teve média {aluno["media"]} e ficou de {aluno["situação"]}.')
else:
    aluno['situação'] = 'REPROVADO'
    print(f'O {aluno["nome"]} teve média {aluno["media"]} e foi {aluno["situação"]}.')
print()
for k, v in aluno.items():
    print(f'A {k} é igual a {v}')
