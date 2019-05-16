class Medidas(object):

    def __init__(self):
        self.__pressao = [0, 0.5, 1]
        self.__temperatura = [23, 273, 423]
        self.__velocidade = [0, 400, 800]
        self.__altitude = [0, 50, 100]

    def temperatura(self):
        return self.__temperatura

    def pressao(self):
        return self.__pressao

    def velocidade(self):
        return self.velocidade

    def altitude(self):
        return self.__altitude

