#Exercício 06
'''Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o 
número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.'''
import time
import os

class Televisor():
    def __init__(self, canal=1, volume=30):
        self.canal = canal
        self.volume = volume
    
    def menu(self):
        while True:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print('TV PYTHON 3 - OPÇÕES')
            print('-' *30)
            print('[1] - MUDA DE CANAL\n[2] - MUDA VOLUME\n[3] - DESLIGA TV')
            print('-' *30)
            print('CANAL: {}'   .format(self.canal))
            print('VOLUME: {}\n'.format(self.volume))
            opcao = int(input('>> '))
            if opcao == 1:
                self.muda_canal()
                break
            elif opcao == 2:
                self.muda_volume()
                break
            elif opcao == 3:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('[3] - TV DESLIGADA\n')
                break
            else:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nOPÇÃO INVÁLIDA!')
                time.sleep(1)
                print('\n\nINFORME COMO INDICADO NO MENU OPÇÕES')
                time.sleep(3)

    def muda_canal(self):
        while True:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print('[1] - MUDA DE CANAL')
            print('CANAL: {}\n' .format(self.canal))
            novo_canal = int(input('NOVO CANAL: '))
            if (novo_canal > 0) and (novo_canal < 100):
                self.canal = novo_canal
                self.menu()
                break
            else:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nCANAL INVÁLIDO')
                time.sleep(1)
                print('\n\nCANAIS DISPONÍVEIS: 1 AO 99.')
                time.sleep(3)
    
    def muda_volume(self):
        while True:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print('[2] - MUDA VOLUME')
            print('CANAL: {}\n' .format(self.volume))
            novo_volume = int(input('NOVO VOLUME: '))
            if (novo_volume > 0) and (novo_volume <= 100):
                self.volume = novo_volume
                self.menu()
                break
            else:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nVOLUME INVÁLIDO!')
                time.sleep(1)
                print('\n\nVOLUME MÍNIMO: 1\nVOLUME MÁXIMO: 100.')
                time.sleep(3)

t = Televisor()
t.menu()
