# -*- coding: UTF-8 -*-
import random
import os

class Adivinhacao():

    def __init__(self, total_de_tentativas):
        self.total_de_tentativas = total_de_tentativas

    def jogar(self, nome):
        print("*********************************")
        print("Bem vindo no jogo de adivinhação!")
        print("         Bora jogar {}           ".format(nome))
        print("*********************************")

        self.__pontos = 0
        numero_secreto = self.numero_secreto()

        for rodada in range(1, self.total_de_tentativas + 1):
            print("Tentativa {} de {}".format(rodada, self.total_de_tentativas))
            chute_invalido, chute = self.chute()

            if not chute_invalido:
                chute_correto = self.valida_chutes(chute, numero_secreto)
                if (chute_correto):
                    self.limpar()
                    return self.__pontos
            else:
                print("Você deve digitar um número entre 1 e 100")

        print("Fim de Jogo!")

    def numero_secreto(self):
        return random.randrange(1, 101)

    def chute(self):

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)
        return (chute < 1 or chute > 100), chute

    def valida_chutes(self, chute, numero_secreto):

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
               print("Você acertou!")
               return True
            elif(maior):
               print("Você errou! Seu chute é maior que o número secreto!")
            elif(menor):
                print("Você errou! Seu chute é menor que o número secreto!")

            self.pontuacao(numero_secreto, chute)

            return False

    def pontuacao(self, numero_secreto, chute):
        pontos_perdidos = abs(numero_secreto - chute)
        self.__pontos += pontos_perdidos

    def limpar(self):
        # if os.name == "nt":
        #     os.system("clear") or None
        # else:
        os.system("cls") or None

if(__name__ == "__main__"):
    Adivinhacao(20).jogar("teste")
