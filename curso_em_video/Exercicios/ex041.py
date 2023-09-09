from datetime import date
ano = date.today().year
nascimento = int(input('Qual ano do seu nascimento? '))
idade = ano - nascimento
if idade < 9:
    print('Você tem {} anos e está na modalidade \033[4mMIRIM'.format(idade))
elif 14> idade >=9:
    print('Você tem {} anos e está na modalidade \033[4mINFANTIL'.format(idade))
elif 19> idade >=14:
    print('Você tem {} anos e está na modalidade \033[4mJUNIOR'.format(idade))
elif 20> idade >=19:
    print('Você tem {} anos e está na modalidade \033[4mSÊNIOR'.format(idade))
else:
    print('Você tem {} anos e está na modalidade \033[4mMASTER'.format(idade))
