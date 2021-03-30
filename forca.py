# -*- coding: UTF-8 -*-
from palavras_secretas import PalavrasSecretas as ps

class Forca():
    def __init__(self):
        self.linhas_utilizadas = []

    def jogar(self):
        self.cabecalho()
        continuar = True

        while(continuar):
            palavra_secreta = self.inicializa_rodada()

            enforcou = False
            acertou = False

            while(not enforcou and not acertou):
                self.boneco_forca(self.erros)
                chute = input("Qual letra ? ").strip().upper()

                if(self.letra_repetida(chute, self.letras_chute)):
                    print("Letra ionformada já foi utilizada anteriormente")
                else:
                    enforcou, acertou = self.valida_chute(chute, palavra_secreta)

            self.resultado(acertou, palavra_secreta)
            continuar = self.jogar_novamente()

    def inicializa_rodada(self):
        self.erros = 0
        self.letras_acertada = []
        self.letras_chute = []
        palavra_secreta = self.obtem_palavra()
        self.esconde_palavra_secreta(palavra_secreta, self.letras_acertada)
        return palavra_secreta

    def valida_chute(self, chute, palavra_secreta):
        if (chute in palavra_secreta):
            self.confirma_letra(palavra_secreta, chute, self.letras_acertada)
        else:
            self.erros += 1

        self.letras_chute.append(chute)
        print("Letras utilizadas:", self.letras_chute)
        print("Palavra:", self.letras_acertada)

        enforcou = self.erros == 6
        acertou = "_" not in self.letras_acertada

        return enforcou, acertou

    def cabecalho(self):
        print("*********************************")
        print("*  Bem vindo no jogo da Forca!  *")
        print("*********************************")

    def obtem_palavra(self):
        linha = self.linha_aleatoria()
        palavra_arquivo = ps().ler(linha).strip("\n").upper()
        posicao_ponto_virgula = palavra_arquivo.find(";")

        palavra = palavra_arquivo[:posicao_ponto_virgula]
        dica = palavra_arquivo[posicao_ponto_virgula:].strip(";")

        print("Dica:", dica)
        return palavra

    def esconde_palavra_secreta(self, palavra_secreta, letras_acertada):
        # letras_acertada = ["_" for letra in palavra_secreta]
        for letra in palavra_secreta:
            if (letra == " "):
                letras_acertada.append("#")
            else:
                letras_acertada.append("_")

        print(letras_acertada)

    def letra_repetida(self, chute, letras_chute):
        return chute in letras_chute

    def confirma_letra(self, palavra_secreta, chute, letras_acertada):
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertada[index] = letra.upper()
            index += 1

    def linha_aleatoria(self):
        # repetida = True
        qtd_repetidas = 0
        qtd_linhas = ps().quantidade_linhas()

        # while(repetida):
        while(True):
            linha_obtida = ps().linha_aleatoria(qtd_linhas)

            if (qtd_linhas == qtd_repetidas):
                continuar = input("Todas as palavras já foram jogadas. Deseja continuar jogando? (Y/N)").strip().upper()
                if (continuar == "Y"):
                    self.linhas_utilizadas.clear()
                    qtd_repetidas = 0
                else:
                    quit()
            elif linha_obtida in self.linhas_utilizadas:
                # repetida = True
                qtd_repetidas += 1
            else:
                # repetida = False
                self.linhas_utilizadas.append(linha_obtida)
                return linha_obtida

        # return linha_obtida

    def jogar_novamente(self):
        continuar_jogando = input("Deseja continuar jogando? (Y/N)").strip().upper()

        if (continuar_jogando == "Y"):
            return True
        else:
            return False

    def resultado(self, acertou, palavra):
        if (acertou):
            print("Você ganhou!")
        else:
            print("Você perdeu! A palavra secreta é", palavra)

        print("Fim de Jogo!")

    def boneco_forca(self, erros):
        if (erros == 1):
            print("┌--┐  ")
            print("|  |  ")
            print("|  O  ")
            print("|     ")
            print("|     ")
            print("|     ")
            print("└-----")
        elif (erros == 2):
            print("┌--┐  ")
            print("|  |  ")
            print("|  O  ")
            print("|  |  ")
            print("|     ")
            print("|     ")
            print("└-----")
        elif (erros == 3):
            print("┌--┐  ")
            print("|  |  ")
            print("|  O  ")
            print("| /|  ")
            print("|     ")
            print("|     ")
            print("└-----")
        elif (erros == 4):
            print("┌--┐  ")
            print("|  |  ")
            print("|  O  ")
            print("| /|\ ")
            print("|     ")
            print("|     ")
            print("└-----")
        elif (erros == 5):
            print("┌--┐  ")
            print("|  |  ")
            print("|  O  ")
            print("| /|\ ")
            print("| /   ")
            print("|     ")
            print("└-----")
        elif (erros == 6):
            print("┌--┐  ")
            print("|  |  ")
            print("|  O  ")
            print("| /|\ ")
            print("| / \ ")
            print("|     ")
            print("└-----")
        else:
            print("┌--┐  ")
            print("|  |  ")
            print("|     ")
            print("|     ")
            print("|     ")
            print("|     ")
            print("└-----")

if(__name__ == "__main__"):
    Forca().jogar()
