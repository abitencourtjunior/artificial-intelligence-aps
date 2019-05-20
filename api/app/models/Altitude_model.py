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
        self.__altitude_percentual = calculo.funcao_tringular()

    def defuzzifucacao_altitude(self):
        if (self.__altitude_percentual <= 0.09 and self.__altitude_atual <= 1000):
            return f'Altitude muito baixa: {self.__altitude_percentual}'
        elif (self.__altitude_percentual > 0.1 and self.__altitude_percentual <= 0.18 and self.__altitude_atual <= 2500):
            return f'Altitude pouco baixa: {self.__altitude_percentual}'
        elif (self.__altitude_percentual > 0.18 and self.__altitude_percentual <= 0.32 and self.__altitude_atual <= 3500):
            return f'Altitude baixa: {self.__altitude_percentual}'
        elif (self.__altitude_percentual > 0.32 and self.__altitude_percentual <= 0.55 and self.__altitude_atual <= 5500):
            return f'Altitude pouco alta: {self.__altitude_percentual}'
        elif (self.__altitude_percentual > 0.55 and self.__altitude_percentual <= 0.71 and self.__altitude_atual <= 7200):
            return f'Altitude alta: {self.__altitude_percentual}'
        elif (self.__altitude_percentual > 0.71 and self.__altitude_percentual <= 0.89 and self.__altitude_atual <= 8800):
            return f'Altitude pouco acima: {self.__altitude_percentual}'
        elif (self.__altitude_percentual > 0.89 and self.__altitude_percentual <= 0.92 and self.__altitude_atual <= 9200):
            return f'Altitude pouco muito acima: {self.__altitude_percentual}'
        elif (self.__altitude_percentual > 0.92 and self.__altitude_percentual <= 0.98 and self.__altitude_atual <= 9800):
            return f'Altitude muito acima: {self.__altitude_percentual}'
        elif (self.__altitude_percentual == 1 and self.__altitude_atual <= 10000):
            return f'Altitude muito alta, cuidado: {self.__altitude_percentual}'
        elif (self.__altitude_atual > 10000):
            return f'Você realmente está muito alto, saiba o que está fazendo, cuidado: {self.__altitude_percentual}'
    @property
    def altitude_taxa(self):
        return self.__altitude_percentual

teste = AltitudeModel(14000)
teste.calculo_fuzzy()
print(teste.altitude_taxa)
print(teste.defuzzifucacao_altitude())

