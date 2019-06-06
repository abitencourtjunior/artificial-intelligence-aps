import sys
sys.path.append("..")

from services.Triangular import Triangular
from services.Conversor import Conversor

class VelocidadeModel(object):

    def __init__(self, velocidade_atual):
        self.__velocidade_atual = velocidade_atual
        self.__velocidade_percentual = 0
        self.__conversao = Conversor()

    def calculo_fuzzy(self):
        calculo = Triangular(self.__velocidade_atual, [100, 400, 800])
        self.__velocidade_percentual = calculo.funcao_tringular()

    def defuzzificacao_temperatura(self):
        if (self.__velocidade_percentual <= 0 and self.__velocidade_atual <= 100):
            return f'Velocidade baixa {self.__velocidade_percentual}'
        elif (self.__velocidade_percentual > 0.1 and self.__velocidade_percentual <= 0.7 and self.__velocidade_atual > 100 and self.__velocidade_atual <= 300):
            return f'Velocidade Média {self.__velocidade_percentual}'
        elif (self.__velocidade_percentual > 0.7 and self.__velocidade_percentual <= 1 or self.__velocidade_atual > 300 or self.__velocidade_atual == 800):
            return f'Velocidade Alta {self.__velocidade_percentual}'

    @property
    def velocidade_taxa(self):
        return self.__velocidade_percentual

# teste = VelocidadeModel(250)
# teste.calculo_fuzzy()
# print(teste.velocidade_taxa)
# print(teste.defuzzificacao_temperatura())