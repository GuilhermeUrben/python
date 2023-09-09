class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor = self.cor_tinta

    def get_cor(self):
        return self.cor


def mostrar(caneta):
    return caneta.cor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)
