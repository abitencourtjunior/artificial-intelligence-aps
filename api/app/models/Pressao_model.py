import sys
sys.path.append("..")

from services.Triangular import Triangular
from services.Medidas import Medidas
from services.Conversor import Conversor

class PressaoModel(object):

    def __init__(self, pressao_atual):
        self.__pressao_atual = pressao_atual
        self.__pressao_percentual = 0
        self.__medida = Medidas()
        self.__conversao = Conversor()

    def calculo_fuzzy(self):
        calculo = Triangular(self.__pressao_atual, [0, 0.5, 1])
        self.__pressao_percentual = calculo.funcao_tringular()