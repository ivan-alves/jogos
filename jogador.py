
class Jogador():
    def __init__(self, nome):
        self.__nome = nome
        self.__pontos = 1000

    def __str__(self):
        return "{} com {} pontos".format(self.__nome, self.__pontos)

    @property
    def nome(self):
        return self.__nome

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos_perdidos):
        self.__pontos -= pontos_perdidos