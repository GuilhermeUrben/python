# string = 'Guilherme'
# print(string.upper())
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Guilherme', 'Urben')
# p1.nome = 'Guilherme'
# p1.sobrenome = 'Urben'

p2 = Pessoa('Carlos', 'Joao')
# p2.nome = 'Carlos'
# p2.sobrenome = 'Joao'



print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
