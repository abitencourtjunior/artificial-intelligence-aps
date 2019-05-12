class ControleDeVoo(object):

    def __init__(self, altitude, pressao, temperatura, velocidade):
        if self.verifica_ternario(altitude):
            if self.verifica_ternario(pressao):
                if self.verifica_ternario(temperatura):
                    if self.verifica_ternario(velocidade):
                        self.__altitude = altitude
                        self.__temperatura = temperatura
                        self.__pressao = pressao
                        self.__velocidade = velocidade
                    else:
                        self.mensagen_erro('Velocidade')
                else:
                    self.mensagen_erro('Temperatura')
            else:
                self.mensagen_erro('Pressão')
        else:
            self.mensagen_erro('Altitude')

    def get_altitude(self):
        return self.__altitude

    def get_pressao(self):
        return self.__pressao

    def get_velocidade(self):
        return self.__velocidade

    def get_temperatura(self):
        return self.__temperatura

    def set_altitude(self, altitude):
        if self.verifica_ternario(altitude):
            self.__altitude = altitude
        else:
            self.mensagen_erro('altitude')

    def set_velocidade(self, velocidade):
        if self.verifica_ternario(velocidade):
            self.__velocidade = velocidade
        else:
            self.mensagen_erro('velocidade')

    def set_pressao(self, pressao):
        if self.verifica_ternario(pressao):
            self.__pressao = pressao
        else:
            self.mensagen_erro('pressao')

    def set_temperatura(self, temperatura):
        if self.verifica_ternario(temperatura):
            self.__temperatura = temperatura
        else:
            self.mensagen_erro('temperatura')

    def verifica_nao_numero(self, amostra):
        if type(amostra) == int or type(amostra) == float:
            return True
        else:
            return False

    def verifica_ternario(self, amostra):
        if self.verifica_nao_numero(amostra):
            if amostra >= self.__medida_zero:
                return True
            else:
                return False
        else:
            return False

    def mensagen_erro(self, variavel):
        mensagen = variavel + ' incorreta! Favor inserir o dado correto!'
        print(mensagen)
        return False