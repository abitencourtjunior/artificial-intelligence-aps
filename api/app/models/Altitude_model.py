import sys
sys.path.append("..")

from services.Triangular import Triangular
from services.Medidas import Medidas
from services.Conversor import Conversor
from models.Temperatura_model import Temperatura_Model

class AltitudeModel(object):

    def __init__(self, altitude_atual):
        self.__altitude_atual = altitude_atual
        self.__altitude_percentual = 0
        self.__medida = Medidas()
        self.__conversao = Conversor()
        self.__temperatura = Temperatura_Model(self.__calcula_temperatura_real())

    def __calcula_temperatura_real(self):
        temperatura = ((self.__altitude_atual * 0.3048) * -2)
        return temperatura

    def temperatura_atual(self):
        return self.__temperatura.valor_atual()

    def calculo_fuzzy(self):
        calculo = Triangular(self.__altitude_atual, self.__medida.altitude())
        self.__altitude_percentual = 100 * calculo.funcao_tringular()

    @property
    def altitude_taxa(self):
        return self.__altitude_percentual


teste = AltitudeModel(12000)
print(teste.temperatura_atual())

