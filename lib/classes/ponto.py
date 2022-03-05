class Ponto:
    def __init__(self, data, e1, s1, e2, s2) -> None:
        self.data = data
        self.entrada1 = e1
        self.saida1 = s1
        self.entrada2 = e2
        self.saida2 = s2
    def getData(self):
        return self.data

    def getEntrada1(self):
        return self.entrada1