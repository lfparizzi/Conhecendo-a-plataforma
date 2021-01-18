# criando um programa básico
from time import sleep
from random import randint

jogadas = ("pedra", "papel", "tesoura")
IA = randint(0,2)

inicio= int(input("Escolha uma jogada: \n[0] Pedra \n[1] Papel \n[2] Tesoura \nFavor digitar o número da jogada:"))

# cosmética do jogo
print('JO\n')
sleep(0.5)
print('KEN\n')
sleep(0.5)
print('PO!\n')
sleep(1)

# jogo
print("#"*31)
print("A IA escolheu: {}".format(jogadas[IA]))
print("Você escolheu: {}".format(jogadas[inicio]))
print("#"*31)
print("\n")

# Demonstração resultado -=- 0-pedra, 1-papel, 2-tesoura

# IA joga pedra
if IA == 0:
    if inicio == 0:
        print('Empatou')
    elif inicio == 1:
        print('Você GANHOU!!!')
    elif inicio == 2:
        print('Perdeu mermão, tenta denovo')
    else:
         print('ué, deu ruim')

# IA joga papel
if IA == 1:
    if inicio == 0:
        print('Perdeu mermão, tenta denovo')
    elif inicio == 1:
        print('Empatou')
    elif inicio == 2:
        print('Você GANHOU!!!')
    else:
         print('ué, deu ruim')

# IA joga tesoura
if IA == 2:
    if inicio == 0:
        print('Você GANHOU!!!')
    elif inicio == 1:
        print('Perdeu mermão, tenta denovo')
    elif inicio == 2:
        print('Empatou')
    else:
         print('ué, deu ruim')

#fim do código, talvez eu coloque algum cosmético no final.
