class Foo:
    def __int__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        print(self.__exemplo)
        self._metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def _metodo_private(self):
        print('_metodo_private')
        return '_metodo_private'


f = Foo()
print(f._protected)
# print(f.public)
# print(f.metodo_publico())
