# -*- coding: UTF-8 -*-
import os.path
import random

class PalavrasSecretas():

    def palavras_secretas(self):
        continuar = True

        while(continuar):
            self.criar_arquivo()
            resposta = input("Deseja continuar (Y/N): ").strip().upper()

            print(resposta)
            if(resposta == "Y"):
                continuar = True
            else:
                continuar = False

    def adicionar(self):
        palavra = input("Insira uma nova palavra: ")
        dica = input("Insira uma nova dica: ")

        with open("palavras.txt", "a") as arquivo_palavra:
            arquivo_palavra.write(palavra + ";" + dica + "\n")

    def ler(self, linha):
        with open("palavras.txt", "r") as arquivo:
            palavra = self.palavra_aleatoria(arquivo, linha)
        return str(palavra)

    def palavra_aleatoria(self, arquivo, linha_arquivo):
        index = 0

        for palavra in arquivo:
            if(linha_arquivo == index):
                return palavra
            index += 1

    def quantidade_linhas(self):
        qtd = 0

        with open("palavras.txt", "r") as arquivo:
            # return len(arquivo)
            for linhas in arquivo:
                qtd += 1
        return qtd

    def linha_aleatoria(self, qtd):
        return random.randrange(0, qtd)

    def criar_arquivo(self):
        exite = os.path.exists("palavras.txt")

        if (exite):
            self.adicionar()
        else:
            arquivo = open("palavras.txt", "w")
            arquivo.close()
            self.adicionar()

if(__name__ == "__main__"):
    PalavrasSecretas().palavras_secretas()
