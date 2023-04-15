class Ordenadora:
    def __init__(self, lista):
        self.listaBaguncada = None

    @classmethod
    def ordenacaoCrescente(cls):
        lista = [3, 4, 2, 1, 5]
        lista.sort()
        print(lista)
        return lista

    @classmethod
    def ordenacaoDecrescente(cls):
        lista1 = [9, 7, 6, 8]
        lista1.sort(reverse=True)
        print(lista1)
        return lista1


crescente = Ordenadora.ordenacaoCrescente()
decrescente = Ordenadora.ordenacaoDecrescente()

