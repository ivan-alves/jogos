import os.path
import random


def adicionar():
    palavra = input("Insira uma nova palavra: ")
    dica = input("Insira uma nova dica: ")

    with open("palavras.txt", "a") as arquivo_palavra:
        arquivo_palavra.write(palavra + ";" + dica + "\n")


def ler(linha_aleatoria):
    with open("palavras.txt", "r") as arquivo:
        palavra = palavra_aleatoria(arquivo, linha_aleatoria)
    return str(palavra)


def quantidade_linhas():
    qtd = 0
    with open("palavras.txt", "r") as arquivo:
        for linhas in arquivo:
            qtd +=1
    return qtd


def palavra_aleatoria(arquivo, quantidade_linhas):
    index = 0

    for palavra in arquivo:
        if(quantidade_linhas == index):
            palavra_secreta = palavra
            break
        index +=1

    return palavra_secreta


def linha_aleatoria(qtd):
    return random.randrange(0, qtd)


def criar_arquivo():
    exite = os.path.exists("palavras.txt")

    if (exite):
        adicionar()
    else:
        arquivo = open("palavras.txt", "w")
        arquivo.close()
        adicionar()


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
