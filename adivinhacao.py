import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    #numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 20
    pontos = 1000
    #rodada = 1

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel_correto = False

    while(not nivel_correto) :
        nivel = int(input("Define o Nível: "))

        if(nivel == 1):
            total_de_tentativas = 20
            nivel_correto = True
        elif(nivel == 2):
            total_de_tentativas = 10
            nivel_correto = True
        elif(nivel == 3):
            total_de_tentativas = 5
            nivel_correto = True
        else:
            print("Nível informado inválido. (1) Fácil (2) Médio (3) Difícil")

    #while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
           print("Você acertou! você fez {} pontos!".format(pontos))
           break
        elif(maior):
           print("Você errou! Seu chute é maior que o número secreto!")
        elif(menor):
            print("Você errou! Seu chute é menor que o número secreto!")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

        #rodada += 1

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()
