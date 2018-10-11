# -*- coding: utf-8 -*-

import random

print("*******************************")
print("Bem vindo ao jogo de Advinhacao")
print("*******************************")

numero_secreto = random.randrange(1,51)
total_de_tentativas = 0
total_pontos = 1000

print(numero_secreto)

print("Escolha o nível de dificuldade")
print("(1) Fácil - (2) Médio - (3) Difícil")

nivel = input("Escolha: ")
nivel = int(nivel)

if(nivel == 1):
    total_de_tentativas = 20
if(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5   

print("JOGO INICIADO")
print("")
print("")

for rodada in range(1, total_de_tentativas+1):
    print("RODADA {} de {}".format(rodada, total_de_tentativas))
    
    chute = input("Digite o seu numero (entre 1 e 50):  ")
    print("Voce digitou o numero", chute, sep=": ")
    chute = int(chute)
    
    if(chute < 1 or chute > 50):
        print("VOCE DIGITOU UM VALOR INVALIDO")
        print("DIGITE UM NUMERO ENTRE 1 E 50!!!!")
        continue

    acertou = numero_secreto==chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("VOCE ACERTOU E TERMINOU COM {} PONTOS".format(total_pontos))
        break
    else:
        if(maior):
            print("VOCE ERROU - LAMENTO")
            print("CHUTE MAIS ALTO QUE O NUMERO SECRETO!!!")
        elif(menor):
            print("VOCE ERROU - LAMENTO")
            print("CHUTE MAIS baixo QUE O NUMERO SECRETO!!!")
        pontos_perdidos = abs(numero_secreto - chute)
        total_pontos = total_pontos - pontos_perdidos
print("*FIM DO JOGO*")
