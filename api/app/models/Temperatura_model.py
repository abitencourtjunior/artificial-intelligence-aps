import sys
sys.path.append("..")

from services.Triangular import Triangular
from services.Medidas import Medidas
from services.Conversor import Conversor

class Temperatura_Model(object):

    def __init__(self, valor=None):
        self.__valor = valor
        self.__taxa = 0
        self.__parametros = Medidas()
        self.__conversao = Conversor()

    def calculo_fuzzy(self):
        calculo = Triangular(self.__valor, self.__parametros.temperatura())
        self.__taxa = calculo.funcao_tringular()

    def defuzzificacao_temperatura(self):
        if(self.__taxa <= 0.8 and self.__valor < 25):
            return f' Era do Gelo {self.__taxa}'
        elif (self.__taxa > 0.1 and self.__taxa <= 0.3 and self.__valor > 25 and self.__valor <= 270):
            return f' Muito frio {self.__taxa}'
        elif (self.__taxa > 0.3 and self.__taxa <= 0.5 and self.__valor > 25 and self.__valor <= 270):
            return f' Frio {self.__taxa}'
        elif (self.__taxa > 0.5 and self.__taxa <= 0.85 and self.__valor > 280 and self.__valor <= 300):
            return f' Normal {self.__taxa}'
        elif (self.__taxa > 0.7 and self.__taxa <= 0.9 and self.__valor > 300):
            return f' Temperatura Alta {self.__taxa}'
        else:
            return f' Ta pegando fogo bicho {self.__taxa}'

    @property
    def taxa(self):
        return self.__taxa

    def valor_atual(self):
        return self.__valor