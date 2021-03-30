# -*- coding: UTF-8 -*-
import forca
from adivinhacao import Adivinhacao


print("*********************************")
print("*        Escolha seu jogo       *")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo ? "))

if (jogo == 1):
    forca.jogar()
else:
    Adivinhacao().jogar()

