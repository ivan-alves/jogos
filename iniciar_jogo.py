import os

from jogador import Jogador
from jogos import Jogos

class IniciarJogo():
    def __init__(self):
        self.jogadores = []
        self.jogo = Jogos()


    def executar(self):
        self.incricao_de_jogadores()

        for jogador in self.jogadores:
            jogador.pontos = self.jogo.jogar(jogador.nome)

        self.limpar()

        for pontuacao in self.jogadores:
            print(pontuacao)

    def incricao_de_jogadores(self):
        continuar_adicionando = True

        while continuar_adicionando:
            self.jogadores.append(Jogador(str(input("Nome do jogador: "))))

            encerrar_inscricao = input("Continuar adicionando jogadores (Y/N)? ").upper()
            continuar_adicionando = (encerrar_inscricao == "Y")

    def limpar(self):
        # if os.name == "nt":
        #     os.system("clear") or None
        # else:
        os.system("cls") or None

if __name__ == "__main__":
    IniciarJogo().executar()