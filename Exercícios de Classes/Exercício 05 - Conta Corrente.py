#Exercício 05 
'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, 
nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e 
os demais atributos são obrigatórios.'''
import random
import time
import os
import sqlite3

conectar = sqlite3.connect(r'C:\sqlite\bd_teste\bank_new_python.db')
c = conectar.cursor()


class ContaCorrente():
    def __init__(self, conta=0, nome='none', saldo=0.00):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    # MENU PRINCIPAL
    def menu(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('\n   **** BANK NEW PYTHON ****\n', '-' * 30, '\
              \n MENU PRINCIPAL\n', '-' * 30, '\
              \n Informe uma opção:\n  1 - Criar Conta\n  2 - Acessar Conta\n  3 - Depositar\n  4 - Sair\n')
        while True:
            selecao = int(input('Opção: '))
            if selecao == 1:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nOpção %d - NOVA CONTA' % selecao)
                print('-' * 30)
                self.criarConta()
                break
            elif selecao == 2:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nOpção %d - ACESSAR CONTA' % selecao)
                print('-' * 30)
                print('\nMenu em desenvolvimento...\n ')
                time.sleep(2)
                input('Aperte enter para voltar para o menu principal.')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                self.menu()                
                break
            elif selecao == 3:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nOpção %d - DEPOSITO EM CONTA' % selecao)
                print('-' * 30)
                self.depósito()
                break
            elif selecao == 4:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nOpção %d - ENCERRAR APLICAÇÃO' % selecao)
                print('-' * 30)
                print('\nObrigado por utilizar o caixa eletrônico New Python!')
                time.sleep(2)
                os.system('exit')
                break
            else:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print('\nOpção %d - OPÇÃO INVÁLIDA!' % selecao)
                print('-' * 30)
                print('\nPara prosseguir informe:\n 1 - Criar Conta\n 2 - Acessar Conta\n 3 - Sair\n')

    # CRIAR UMA NOVA CONTA
    def criarConta(self):
        dados_nome = input('Digite o nome do titular da conta: ')
        self.nome = dados_nome
        dados_conta = str(random.randrange(1000, 9999)) + '-' + str(random.randrange(1, 9))
        self.conta = dados_conta
        print('Criando conta, aguarde...\n')
        time.sleep(3)
        print('Conta criada com sucesso!\n')
        time.sleep(1)
        self.bancoDados()
        input('\nAperte enter para voltar ao menu principal.')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        self.menu()

    # SALVAR OS DADOS DENTRO DO BANCO DE DADOS  JÁ CRIADO "bank_new_python.db" VIA SQLITE
    def bancoDados(self):
        print('CONTA: {}\nTITULAR: {}\nSALDO: R$ {:.2f}'.format(self.conta, self.nome, self.saldo))
        c.execute('INSERT INTO dados_conta VALUES(?,?,?)', (self.conta, self.nome, self.saldo))
        conectar.commit()

    # def alterarNome(self):

    def depósito(self):
        sql = 'SELECT * FROM dados_conta WHERE conta = ?'
        num = str(input('Digite o número da conta para depósito [xxxx-x]: '))
        for row in c.execute(sql, (num,)):

            if row[0] == num:
                valor = float(input('Valor: R$ '))
                c.execute('UPDATE dados_conta SET saldo = saldo + ? WHERE conta = ?', (valor, num))
                conectar.commit()
                time.sleep(3)
                print('\nDepósito realizado com sucesso!\n')
                time.sleep(1)
                input('\nAperte enter para voltar ao menu principal.')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                self.menu()
contaCorrente = ContaCorrente()
contaCorrente.menu()