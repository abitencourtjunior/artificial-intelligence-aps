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
        self.__valor = self.__conversao.celcius_kelvin(self.__valor)
        calculo = Triangular(self.__valor, self.__parametros.temperatura())
        self.__taxa = 100 *  calculo.funcao_tringular()

    def defuzzificacao_temperatura(self):
        if(self.__valor == 218):
            return f'Temperatura de Vôo: {self.__conversao.kelvin_celcius(self.__valor)} °C - {self.taxa} %'
        # Falta colocar mais validações no sistema.

    @property
    def taxa(self):
        return self.__taxa

    def valor_atual(self):
        return self.__valor

teste = Temperatura_Model(-55)
teste.calculo_fuzzy()
print(teste.taxa)
print(teste.valor_atual())
print(teste.defuzzificacao_temperatura())