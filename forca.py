#import random
import palavras_secretas as palavras

linhas_utilizadas = []

def jogar():
    cabecalho()
    continuar = True

    while(continuar):
        palavra_secreta = palavra_aleatoria()
        letras_acertada = []
        esconde_palavra_secreta(palavra_secreta, letras_acertada)

        enforcou = False
        acertou = False
        erros = 0
        letras_chute = []

        while(not enforcou and not acertou):
            chute = input("Qual letra ? ").strip().upper()

            if(letra_repetida(chute,letras_chute)):
                print("Letra ionformada já foi utilizada anteriormente")
            else:
                if (chute in palavra_secreta):
                    confirma_letra(palavra_secreta, chute, letras_acertada)
                    boneco_forca(erros)
                else:
                    erros +=1
                    boneco_forca(erros)

                letras_chute.append(chute)
                print("Letras utilizadas:", letras_chute)
                print("Palavra:",letras_acertada)

                enforcou = erros == 6
                acertou = "_" not in letras_acertada

        resultado(acertou, palavra_secreta)
        continuar = jogar_novamente()

def esconde_palavra_secreta(palavra_secreta, letras_acertada):
    # letras_acertada = ["_" for letra in palavra_secreta]
    for letra in palavra_secreta:
        if (letra == " "):
            letras_acertada.append("#")
        else:
            letras_acertada.append("_")

    print(letras_acertada)

def letra_repetida(chute, letras_chute):
    return chute in letras_chute

def linha_aleatoria():
    repetida = True
    qtd_repetidas = 0
    qtd_linhas = palavras.quantidade_linhas()

    while(repetida):
        linha_obtida = palavras.linha_aleatoria(qtd_linhas)
        if (qtd_linhas == qtd_repetidas):
            continuar = input("Todas as palavras já foram jogadas. Deseja continuar jogando? (Y/N)").strip().upper()
            if (continuar == "Y"):
                linhas_utilizadas.clear()
                qtd_repetidas = 0
        elif linha_obtida in linhas_utilizadas:
            repetida = True
            qtd_repetidas += 1
        else:
            repetida = False
            linhas_utilizadas.append(linha_obtida)

    return linha_obtida

def palavra_aleatoria():
    linha = linha_aleatoria()
    dica_palavra_secreta(linha)
    return palavras.ler("palavras.txt", linha).strip("\n").upper()
    # return palavra_secreta

def dica_palavra_secreta(linha):
    dica = palavras.ler("dica.txt", linha).strip("\n").upper()
    print("Dica:", dica)


def jogar_novamente():
    continuar_jogando = input("Deseja continuar jogando? (Y/N)").strip().upper()
    if (continuar_jogando == "Y"):
        continuar = True
    elif (continuar_jogando == "N"):
        continuar = False
    else:
        continuar = False

    return continuar


def cabecalho():
    print("*********************************")
    print("*  Bem vindo no jogo da Forca!  *")
    print("*********************************")


def confirma_letra(palavra_secreta,chute,letras_acertada):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertada[index] = letra.upper()
        index += 1


def resultado(acertou, palavra):
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu! A palavra secreta é", palavra)

    print("Fim de Jogo!")


def boneco_forca(erros):
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
    jogar()
