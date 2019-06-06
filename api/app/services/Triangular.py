import numpy as np

class Triangular(object):

    def __init__(self, valor, plano):
        self.__valor = valor
        if(len(plano) == 3):
            self.__plano = plano

    def calcular_parametros(self):
        parametrox = (self.__valor - self.__plano[0]) / (self.__plano[1] - self.__plano[0])
        parametroy = (self.__plano[2] - self.__valor) / (self.__plano[2] - self.__plano[1])
        return [parametrox, parametroy]

    def funcao_tringular(self):
        fuzzyficacao = np.max(np.min(self.calcular_parametros()),0)
        return fuzzyficacao

# Testes de Funcionalidades
# control_fuzzy = Triangular(290, [1,2,3])
# print(control_fuzzy.funcao_tringular())

