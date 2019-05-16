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
