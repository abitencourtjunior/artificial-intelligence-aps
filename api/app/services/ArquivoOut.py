import os.path

class ArquivoOut(object):

    __saida = 'terminal'

    def get_saida(self):
        return self.__saida

    def set_saida(self, saida):
        if saida == "terminal" or saida == "txt":
            self.__saida = saida
        else:
            print("tipo de saida nao reconhecida")
            return False

    def output(self, saida=None):
        if self.__saida == "txt":
            if os.path.isfile('./output.txt'):
                arquivo = open('log.txt', 'r')
                conteudo = arquivo.readlines()
                conteudo.append(saida)
                arquivo = open('log.txt', 'w')
                arquivo.writelines(conteudo)
                arquivo.close()
            else:
                pass
        elif self.__saida == "terminal":
            print(saida)
        else:
            print("tipo de saida nao reconhecida")
            return False