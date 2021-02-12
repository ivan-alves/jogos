#import random
import palavras_secretas as palavras

def jogar():
    print("*********************************")
    print("*  Bem vindo no jogo da Forca!  *")
    print("*********************************")

    palavra_secreta = palavras.ler().strip("\n").upper()

    enforcou = False
    acertou = False
    erros = 0
    #     letras_acertada.append("_")
    # for letra in palavra_secreta:
    letras_acertada = ["_" for letra in palavra_secreta]


    print(letras_acertada)

    while(not enforcou and not acertou):

        chute = input("Qual letra ? ").strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertada[index] = letra.upper()
                    # print("Encontrei a letra {} na posição {}".format(chute, index))
                index += 1
            boneco_forca(erros)
        else:
            erros +=1

            boneco_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertada
        print(letras_acertada)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

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
