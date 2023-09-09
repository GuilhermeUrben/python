class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor    
    
    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor    


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


uno = Carro('Uno')
fiat = Fabricante('Fiat')
motor_1_0 = Motor('1.0')
uno.fabricante = fiat
uno.motor = motor_1_0
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

chevete = Carro('Chevete')
fiat = Fabricante('Ford')
motor_2_0 = Motor('2.0')
chevete.fabricante = fiat
chevete.motor = motor_2_0
print(chevete.nome, chevete.fabricante.nome, chevete.motor.nome)
