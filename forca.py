#import random
import palavras_secretas as palavras

# adicionar validaçâo de letra repetida
# adicionar letras erradas na tela
# tratar espaço de palavra composta
# não repetir a palavra alterior
# mostrar palavra no final de cada jogo
#

def jogar():
    print("*********************************")
    print("*  Bem vindo no jogo da Forca!  *")
    print("*********************************")

    continuar = True
    while(continuar):

        linha_aleatoria = palavras.linha_aleatoria(palavras.quantidade_linhas())
        palavra_secreta = palavras.ler("palavras.txt", linha_aleatoria).strip("\n").upper()
        dica = palavras.ler("dica.txt", linha_aleatoria).strip("\n").upper()

        print("Dica:", dica)

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

        continuar_jogando = input("Deseja continuar jogando? (Y/N)").strip().upper()
        if(continuar_jogando == "Y"):
            continuar = True
        elif (continuar_jogando == "N"):
            continuar = False
        else:
            continuar = False


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
