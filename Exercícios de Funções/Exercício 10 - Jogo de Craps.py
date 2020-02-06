#Exercício 10
# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado
# de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar
# jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente. 

import random
import time

def craps():
    dado = random.randint(2,12)
    return dado

print('\n****Jogo de Craps****\n')
inicio = craps()
numero_jogadas = 1
print('Jogada 1 -> {}' .format(inicio) )
if (inicio == 7) or (inicio == 11):
    print('\nVocê ganhou!\nSoma natural você tirou {}\n' .format(inicio))
elif (inicio == 2) or (inicio == 3) or (inicio == 12):
    print('\nVocê perdeu!\nA soma dos dados foi {} isso é um craps\n' .format(inicio))
else:
    while True:
        numero_jogadas += 1
        nova_jogada = craps()
        time.sleep(2.5)
        print('Jogada {} -> {}' .format(numero_jogadas, nova_jogada))
        if nova_jogada == 7:
            print('\nVocê perdeu!\nA soma é igual a 7 você precisaria de {} (Primeira Jogada) para vencer\n' .format(inicio))
            break
        elif nova_jogada == inicio:
            print('\nVocê venceu!\nTirou o mesmo valor da primeira jogada!\n')
            break
