import sys
sys.path.append("..")

from services.Triangular import Triangular
from services.Medidas import Medidas
from services.Conversor import Conversor

class PressaoModel(object):

    def __init__(self, altitude):
        self.__altitude = altitude
        self.__pressao_percentual = 0

    def __pressao_definida(self):
        if(self.__altitude == 0 and self.__altitude < 1000):
            self.__pressao_percentual = 1
        elif(self.__altitude == 1000 and self.__altitude < 2000):
            self.__pressao_percentual = 600
        elif (self.__altitude == 2000 and self.__altitude < 4000):
            self.__pressao_percentual = 480
        elif (self.__altitude == 4000 and self.__altitude < 6000):
            self.__pressao_percentual = 300
        elif (self.__altitude == 6000 and self.__altitude < 8000):
            self.__pressao_percentual = 170
        elif (self.__altitude == 8000 and self.__altitude < 10000):
            self.__pressao_percentual = 120
        elif (self.__altitude == 10000 and self.__altitude < 14000):
            self.__pressao_percentual = 80
        elif (self.__altitude == 14000 and self.__altitude < 16000):
            self.__pressao_percentual = 60

    @property
    def pressao_taxa(self):
        self.__pressao_definida()
        return self.__pressao_percentual

# teste = PressaoModel(14000)
# teste.pressao_definida()
# print(teste.pressao_taxa)
