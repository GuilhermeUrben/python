from pythonTest.ex115.modulos import *
from time import sleep
from pythonTest.ex115.arquivos import *

arq = 'gui.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar um arquivo
        lerarquivo(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema.. Até logo')
        break
    else:
        # Digitou uma opão errada no menu.
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(2)
