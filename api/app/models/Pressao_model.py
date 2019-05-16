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
        pass