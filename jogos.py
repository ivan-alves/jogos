# -*- coding: UTF-8 -*-
from adivinhacao import Adivinhacao
from forca import Forca

class Jogos():
    def __init__(self):
        self.jogo = self.escolha_o_que_jogar()
        self.total_de_tentativas = self.escolher_dificuldade()

    def escolha_o_que_jogar(self):
        print("*********************************")
        print("*        Escolha seu jogo       *")
        print("*********************************")

        print("(1) Forca (2) Adivinhação")

        return int(input("Qual jogo ? "))

    def jogar(self, nome):

        if self.jogo == 1:
            Forca().jogar()
        else:
            return Adivinhacao(self.total_de_tentativas).jogar(nome)

    def escolher_dificuldade(self):
        print("Qual nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")

        while(True) :
            nivel = int(input("Define o Nível: "))

            if(nivel == 1):
                return 20
            elif(nivel == 2):
                return 10

            elif(nivel == 3):
                return 5
            else:
                print("Nível informado inválido. (1) Fácil (2) Médio (3) Difícil")

if __name__ == "__main__":
    Jogos().escolha_o_que_jogar()