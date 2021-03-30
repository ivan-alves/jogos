# -*- coding: UTF-8 -*-
import random
import os

class Adivinhacao():

    def __init__(self):
        print("*********************************")
        print("Bem vindo no jogo de adivinhação!")
        print("*********************************")
        self.__pontos = 1000

    def jogar(self):

        numero_secreto = self.numero_secreto()
        total_de_tentativas = self.escolher_dificuldade()
        self.limpar()

        for rodada in range(1, total_de_tentativas + 1):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute_invalido, chute = self.chute()
            self.limpar()
            if not chute_invalido:
                chute_correto = self.valida_chutes(chute, numero_secreto)
                if (chute_correto):
                    break
            else:
                print("Você deve digitar um número entre 1 e 100")




        print("Fim de Jogo!")

    def numero_secreto(self):
        return random.randrange(1, 101)

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

    def chute(self):

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)
        return (chute < 1 or chute > 100), chute

    def valida_chutes(self, chute, numero_secreto):

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
               print("Você acertou! você fez {} pontos!".format(self.__pontos))
               return True
            elif(maior):
               print("Você errou! Seu chute é maior que o número secreto!")
            elif(menor):
                print("Você errou! Seu chute é menor que o número secreto!")

            self.pontuacao(numero_secreto, chute)

            return False

    def pontuacao(self, numero_secreto, chute):
        pontos_perdidos = abs(numero_secreto - chute)
        self.__pontos -= pontos_perdidos

    def limpar(self):
        # if os.name == "nt":
        #     os.system("clear") or None
        # else:
        os.system("cls") or None

if(__name__ == "__main__"):
    jogar = Adivinhacao().jogar()
