class Lampada:
    def __init__(self, nome, ligada=False):
        self.nome = nome
        self.ligada = False

    def liga(self):
        self.ligada = True
        return 

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        if self.ligada is True:
            print(f'A lâmpada está ligada?True')
            return True
        if self.ligada is False:
            print('A lâmpada ainda está ligada?False')


l1 = Lampada('1')
l1.liga()
l1.esta_ligada()
l1.desliga()
l1.esta_ligada()