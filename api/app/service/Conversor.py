class Conversor(object):

    def __init__(self, temperatura):
        self.__temperatura = int(temperatura)

    @property
    def temperatura_celcius(self):
        return self.__parametro

    def celcius_kelvin(self):
        if(self.__temperatura >= 0):
            kelvin = self.__temperatura + 273
            return str(kelvin)