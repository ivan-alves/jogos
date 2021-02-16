import os.path
import random



def adicionar():
    arquivo_palavra = open("palavras.txt", "a")
    arquivo_dica = open("dica.txt", "a")

    palavra = input("Insira uma nova palavra: ")
    dica = input("Insira uma nova dica: ")

    arquivo_palavra.write(palavra + "\n")
    arquivo_dica.write(dica + "\n")

    arquivo_palavra.close()
    arquivo_dica.close()

def ler(arquivo,linha_aleatoria):
    arquivo = open(arquivo, "r")

    palavra = palavra_aleatoria(arquivo, linha_aleatoria)
    arquivo.close()
    return str(palavra)

def quantidade_linhas():
    arquivo = open("palavras.txt", "r")
    qtd = 0
    for linhas in arquivo:
        qtd +=1

    arquivo.close()

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
