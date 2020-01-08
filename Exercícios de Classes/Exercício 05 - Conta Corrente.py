#Exercício 05 
'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, 
nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e 
os demais atributos são obrigatórios.'''
import os
import time
import random

dicionario = {}
lista = []

class ContaCorrente():
    def __init__(self, conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def menu_principal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('BANCO NEW PYTHON')
        print('-' *30)
        print('Informe a opção desejada:')
        print('[1] - NOVA CONTA\n[2] - ACESSAR CONTA\n[3] - DEPOSITAR\n[4] - SAQUE\n[5] - ALTERAR NOME\n[6] - SAIR')
        while True:
            opcao = int(input('\n>> '))
            if opcao == 1:
                self.nova_conta()
                break
            elif opcao == 2:
                self.acessa_conta()
                break
            elif opcao == 3:
                self.deposito()
                break
            elif opcao == 4:
                self.saque()
                break
            elif opcao == 5:
                self.alterar_nome()
                break            
            elif opcao == 6:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('[6] - SAIR')
                print('\nAplicação encerrada!\nBANCO NEW PYTHON agradece a preferência!\n\n')
                break
            else:
                print('Opção inválida!')   

    def nova_conta(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('[1] - MENU NOVA CONTA')
        self.nome = input('\nDigite o nome do titular da conta: ')
        self.conta = str(random.randrange(1000, 9999)) + '-' + str(random.randrange(1, 9))        
        dicionario['nome'] = self.nome       
        dicionario['conta'] = self.conta
        dicionario['saldo'] = self.saldo
        lista.append(dicionario.copy())        
        print('\nCriando conta, aguarde...')
        time.sleep(3)  
        print('\nConta criada com sucesso!')
        time.sleep(1)
        print('\nAnote o número da conta: ', self.conta, '\n')
        input('Aperte ENTER para voltar para o MENU PRINCIPAL')
        self.menu_principal()
    
    def acessa_conta(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        validador = False
        print('[2] - MENU DE ACESSO DE CONTA')
        while True:
            dados = input('\nDigite o número da conta [XXXX-X]: ')
            for i in lista:
                if dados == i['conta']:
                    self.conta = i['conta']
                    self.nome = i['nome']
                    self.saldo = i['saldo']
                    validador = True
            if validador == False:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('Conta inválida!')
            else:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('DETALHES DA CONTA:')
                print('\nTitular da conta {}: {} ' .format(self.conta,self.nome) )
                print('Saldo: R$%6.2f\n\n' %self.saldo)               
                break
        input('\nAperte ENTER para voltar para o MENU PRINCIPAL')
        self.menu_principal()

    def deposito(self):
        self.nome = ''
        self.conta = 0
        self.saldo = 0.00
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        validador = False 
        print('[3] - DEPÓSITO')
        
        while True:
            dados = input('\nDigite o número da conta para depósito[XXXX-X]: ')
            for i in lista:
                if dados == i['conta']:
                    self.conta = i['conta']
                    self.saldo = i['saldo']
                    self.nome = i['nome']
                    validador = True
            if validador == False:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('Conta inválida!')
            else:
                break
        while True:
            valor = float(input('Digite o valor do depósito: R$ '))
            if valor <= 0:
                print('Valor inválido!')
            else:
                for i in lista:
                    if dados == i['conta']:
                        self.saldo = self.saldo + valor   
                        i['saldo'] = self.saldo               
                break
        input('\nAperte ENTER para voltar para o MENU PRINCIPAL')
        self.menu_principal()

    def saque(self):
        self.nome = ''
        self.conta = 0
        self.saldo = 0.00
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        validador = False 
        print('[4] - SAQUE')        
        while True:
            dados = input('\nDigite o número da conta para saque[XXXX-X]: ')
            for i in lista:
                if dados == i['conta']:
                    self.conta = i['conta']
                    self.saldo = i['saldo']
                    self.nome = i['nome']
                    validador = True
            if validador == False:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('Conta inválida!')
            else:
                break
        validador = False
        while True:
            saque = float(input('Valor: R$ '))
            for i in lista:
                if dados == i['conta']:
                    if saque > i['saldo']:
                        print('O saldo não é suficiênte! ')
                    else:
                        print('Saque realizado com sucesso!')
                        self.saldo = self.saldo - saque   
                        i['saldo'] = self.saldo 
                        validador = True
            if validador == True:
                break
        input('\nAperte ENTER para voltar para o MENU PRINCIPAL')
        self.menu_principal() 

    def alterar_nome(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        validador = False
        print('[5] - ALTERAR NOME')
        while True:
            dados = input('\nDigite o número da conta para alterar o nome do titular[XXXX-X]: ')
            for i in lista:
                if dados == i['conta']:
                    self.conta = i['conta']
                    self.saldo = i['saldo']
                    nome_antigo = i['nome']
                    i['nome'] = input('Digite o novo nome: ')
                    self.nome = i['nome']
                    validador = True
            if validador == False:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('Conta inválida!')
            else:
                print('\nNome alterado de "{}" para "{}" com sucesso!' .format( nome_antigo,self.nome ))
                break
        input('\nAperte ENTER para voltar para o MENU PRINCIPAL')
        self.menu_principal() 

c = ContaCorrente(0,'none',0.00)
c.menu_principal()
