import numpy as np

from model.Medidas import Medidas

class fuzzy:

    def __init__(self, valor, plano):
        self.__valor = valor
        self.__plano = plano

    def calcular_parametros(self):
        parametrox = (self.__valor - self.__plano[0]) / (self.__plano[1] - self.__plano[0])
        parametroy = (self.__plano[2] - self.__valor) / (self.__plano[2] - self.__plano[1])
        return [parametrox, parametroy]

    def funcao_tringular(self):
        fuzzyficacao = np.max(np.min(self.calcular_parametros()),0)
        return fuzzyficacao


parametros = Medidas()
control_fuzzy = fuzzy(243.15, parametros.temperatura())
print(control_fuzzy.funcao_tringular())

