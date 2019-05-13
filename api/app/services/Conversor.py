class Conversor(object):

    def __init__(self):
        pass

    def celcius_kelvin(self, temperatura):
        if(temperatura < 0 or temperatura <= 273):
            kelvin = temperatura + 273
            return kelvin

    def kelvin_celcius(self, temperatura):
        celcius = temperatura - 273
        return celcius

    @property
    def temperatura_celcius(self):
        return self.__parametro