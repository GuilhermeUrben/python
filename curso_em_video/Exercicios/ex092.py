from datetime import date
atual = date.today().year
fgts = dict()
aposentar = 35

fgts['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
fgts['idade'] = atual - ano
carteira = int(input('Carteira de Trabalho [Digite \033[4m0\033[m caso não tenha]: '))
if carteira != 0:
    fgts['ctps'] = carteira
    fgts['contratado'] = int(input('Ano de contratação: '))
    fgts['salario'] = int(input('Salário : R$ '))
    servico = atual - fgts['contratado']
    aposentar = (35 - servico) + fgts['idade']
    print()
    print(f'O funcionário {fgts["nome"]} tem {fgts["idade"]} anos e foi contratado no ano de {fgts["contratado"]}, '
          f'com salário de R$ {fgts["salario"]} e se aposentará com {aposentar} anos.')
else:
    fgts['ctps'] = 'Não tem carteira de trabalho.'
    print()
    print(f'{fgts["nome"]} tem {fgts["idade"]} anos e {fgts["ctps"]}')
