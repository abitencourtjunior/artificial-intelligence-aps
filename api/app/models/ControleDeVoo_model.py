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
        #temp, velocidade, pressao, altitude

    def defuzificacao_controle(self):
        defuzzy = self.fuzzificacao_controle()
        if(defuzzy[0] > 0.8 and self.temperatura < 300 and defuzzy[3] < 0.8 and self.altitude >= 8000 and defuzzy[2] > 0.8 ):
            return "Voo Normal - Suas condições são boas para voo"
        elif (defuzzy[0] < 0.8 and self.temperatura <= 400 and defuzzy[3] <= 0.09 or self.altitude <= 1000 and defuzzy[2] > 0.4):
            return "ATENÇÃO - Verifique a temperatura em que está a aeronave"
        elif (defuzzy[0] < 0.8 and self.temperatura <= 400 and defuzzy[3] <= 0.3 or self.altitude >= 3000 and defuzzy[2] > 0.8 ):
            return "Alerta - Aeronave Caindo - Suas condições de voo não são boas"



    @property
    def altitude(self):
        return self.__altitude

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def temperatura(self):
        return self.__temperatura


#temp, velocidade, pressao, altitude
teste = ControleDeVoo(900, 380, 350)
print(teste.fuzzificacao_controle())
print(teste.defuzificacao_controle())
