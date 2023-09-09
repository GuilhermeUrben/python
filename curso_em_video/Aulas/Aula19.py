#'''filme = {'titulo':'Star Wars',
#         'ano':1977,
#         'diretor':'George Lucas'
#         }'''
#'''for k, v in filme.items():
#    print(f'O {k} é {v}')'''

'''locadora = list()
locadora.append(filme)
print(locadora[0]['diretor'])'''

#pessoas = {'nome': 'Guilherme', 'sexo': 'M', 'idade': 26}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.items())
#del pessoas['sexo'],
#pessoas['peso'] = '82.5'
#for k, v in pessoas.items():
#    print(f'o {k} = {v}')

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
