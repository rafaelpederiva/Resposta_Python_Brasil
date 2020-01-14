#Exercício 08
# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), 
# verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo 
# menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o 
# outro. É possível criar um macaco canibal?
import os
import time

lista_alimento = [  {'codigo': 1, 'produto':   'Banana'},{'codigo':  2, 'produto': 'Morango'},
                    {'codigo': 3, 'produto': 'Melancia'},{'codigo':  4, 'produto':    'Maçã'},
                    {'codigo': 5, 'produto':     'Pêra'},{'codigo':  6, 'produto':   'Mamão'},
                    {'codigo': 7, 'produto':  'Laranja'},{'codigo':  8, 'produto':   'Limão'},
                    {'codigo': 9, 'produto':    'Amora'},{'codigo': 10, 'produto':     'Uva'} ]

dicionario = {}
lista = []

class Macaco():

    def __init__(self, nome='', bucho=[]):
        self.nome = nome
        self.bucho = bucho
    
    def limpar_tela(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def nome_macacos(self):
        self.limpar_tela()
        for i in range(0,2):
            dicionario['macaco'] = input('Digite o nome do %dº Macaco: ' %(i + 1))
            dicionario['bucho'] = []
            lista.append(dicionario.copy())           
        self.menu()
    
    def ver_bucho(self):
        for i in lista:
            nome_macaco = i['macaco']
            print('\nEsse é o macaco ==> {}' .format(i['macaco']))
            print(' _________')
            print('@| º U º |@')
            print('  |(===)| ')
            print(' =========')
            for f in i['bucho']:
                if i['macaco'] == nome_macaco:
                    print(' ', f)
            print(' =========')
            print('-'*45)     

    def menu(self):
        self.limpar_tela()
        self.ver_bucho()
        print('Escolha uma opção:')
        print('[1] - ALIMENTAR MACACO\n[2] - DIGERIR ALIMENTO\n[3] - SAIR')
        while True:
            opcao = int(input('\n>> '))
            if opcao == 1:
                self.comer()
                break
            elif opcao == 2:
                self.digerir()
                break
            elif opcao == 3:
                self.limpar_tela()
                print('Encerrado!')
                break
            else:
                print('Opção inválida!!')  

    def comer(self):
        self.limpar_tela()
        self.ver_bucho()
        print('Digite o nome do macaco que você quer alimentar: ')
        validador = False
        while True:
            n = input('\n>> ')
            for i in lista:
                if n == i['macaco']:
                    validador = True
            if validador == True:
                break
            else:
                print('Nome inválido!')
        self.nome = n
        self.limpar_tela()
        self.ver_bucho()
        print('Escolha uma opção para o {}' .format(self.nome))
        for i in lista:
            if i['macaco'] != self.nome:
                print('[1] - Dar comida\n[2] - Dar o macaco {}' .format(i['macaco']))
        while True:
            opcao = int(input('\n>> '))
            if (opcao == 1) or (opcao == 2):
                break
            else:
                print('Valor inválido!!')
        self.limpar_tela()
        self.ver_bucho()
        if opcao == 1:
            print('Escolha uma refeição para o {} (digite o código)' .format(self.nome))
            print('\nCódigo   Produto')
            print('------   -----------')
            for i in lista_alimento:
                print('{:<9}{:<12}' .format(i['codigo'], i['produto']))
            while True:
                opcao = int(input('\n>> '))
                if opcao > len(lista_alimento):
                    print('Opção inválida!')
                else:
                    break
            for i in lista_alimento:
                if opcao == i['codigo']:
                    alimento = i['produto']
            for i in lista:
                if self.nome == i['macaco']:
                    i['bucho'].append(alimento)
                    self.bucho = i['bucho']
            self.menu()
        elif opcao == 2:
            self.limpar_tela()
            for i in lista:
                if i['macaco'] == self.nome:
                    print('\nEsse é o macaco ==> {}' .format(self.nome))
                    print(' _________')
                    print('@| º U º |@')
                    print('  |(===)| ')
                    print(' =========')
                    for f in i['bucho']:
                        if i['macaco'] == self.nome:
                            print(' ', f)
                    for g in lista:
                        if g['macaco'] != self.nome:
                            maca = g['macaco']
                            print('  {}' .format(maca))
                    print('  _______')
                    print(' @|x U x|@')
                    print('   |(¬)| ')
                    print(' =========')
                    print('-'*45)     
                    print('\nO {} comeu o {} ele é um macaco canibal!!\n' .format(self.nome, maca))

    def digerir(self):
        self.limpar_tela()
        self.ver_bucho()
        print('Digite o nome do macaco que você para fazer digestão: ')
        validador = False
        while True:
            n = input('\n>> ')
            for i in lista:
                if n == i['macaco']:
                    validador = True
            if validador == True:
                break
            else:
                print('Nome inválido!')
        self.nome = n
        self.limpar_tela()
        self.ver_bucho()
        for i in lista:
            if i['macaco'] == self.nome:
                i['bucho'] = []
        print('Fazendo digestão...')
        time.sleep(3)
        self.menu()        

m = Macaco()
m.nome_macacos()
