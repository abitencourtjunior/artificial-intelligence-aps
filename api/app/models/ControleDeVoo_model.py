from api.app.models.Temperatura_model import TemperaturaModel
from api.app.models.Velocidade_Model import VelocidadeModel
from api.app.models.Pressao_model import  PressaoModel
from api.app.models.Altitude_model import AltitudeModel

class ControleDeVoo():

    def __init__(self, altitude, velocidade, temperatura):
        self.__altitude = altitude
        self.__temperatura = temperatura
        self.__velocidade = velocidade

    def fuzzificacao_controle(self):
        parametros = []

        temp_model = TemperaturaModel(self.__temperatura)
        temp_model.calculo_fuzzy()
        parametros.append(temp_model.taxa)

        velo_model = VelocidadeModel(self.__velocidade)
        velo_model.calculo_fuzzy()
        parametros.append(velo_model.velocidade_taxa)

        pressao_model = PressaoModel(self.__altitude)
        parametros.append(pressao_model.pressao_taxa)

        altitude_model = AltitudeModel(self.__altitude)
        altitude_model.calculo_fuzzy()
        parametros.append(altitude_model.altitude_taxa)

        return parametros


    @property
    def altitude(self):
        return self.__altitude

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def temperatura(self):
        return self.__temperatura


teste = ControleDeVoo(8000, 380, 278)
teste.fuzzificacao_controle()
