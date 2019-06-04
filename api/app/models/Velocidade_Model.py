import sys
sys.path.append("..")

from services.Triangular import Triangular
from services.Medidas import Medidas
from services.Conversor import Conversor

class VelocidadeModel(object):

    def __init__(self, velocidade_atual):
        self.__velocidade_atual = velocidade_atual
        self.__velocidade_percentual = 0
        self.__medida = Medidas()
        self.__conversao = Conversor()

    def calculo_fuzzy(self):
        calculo = Triangular(self.__velocidade_atual, self.__medida.velocidade())
        self.__velocidade_percentual = calculo.funcao_tringular()

    @property
    def velocidade_taxa(self):
        return self.__velocidade_percentual

teste = VelocidadeModel(50)
teste.calculo_fuzzy()
print(teste.velocidade_taxa)