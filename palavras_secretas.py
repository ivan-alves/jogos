import os.path
import random

def adicionar():
    arquivo = open("palavras.txt", "a")
    palavra_input = input("Insira uma nova palavra: ")
    arquivo.write(palavra_input + "\n")
    arquivo.close()

def ler():
    arquivo = open("palavras.txt", "r")

    palavra = palavra_aleatoria(quantidade_linhas())
    arquivo.close()
    return str(palavra)

def quantidade_linhas():
    arquivo = open("palavras.txt", "r")
    qtd = 0
    for linhas in arquivo:
        qtd +=1

    arquivo.close()

    return qtd

def palavra_aleatoria(quantidade_linhas):
    arquivo = open("palavras.txt", "r")

    aleatorio = random.randrange(0, quantidade_linhas)
    index = 0

    for palavra in arquivo:
        if(aleatorio == index):
            palavra_secreta = palavra
        index +=1

    return palavra_secreta

def criar_arquivo():
    exite = os.path.exists("palavras.txt")

    if (exite):
        adicionar()
    else:
        arquivo = open("palavras.txt", "w")
        arquivo.write(adicionar())
        arquivo.close()

def palavras_secretas():
    continuar = True

    while(continuar):
        criar_arquivo()
        resposta = input("Deseja continuar (Y/N): ").strip().upper()

        print(resposta)
        if(resposta == "Y"):
            continuar = True
        else:
            continuar = False


if(__name__ == "__main__"):
    palavras_secretas()
