#Exercício 07
#Classe Bichinho Virtual. Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# 	> Atributos: Nome, Fome, Saúde e Idade;
# 	> Métodos: Alterar Nome, Fome, Saúde e Idade; 
# 	> Retornar Nome, Fome, Saúde e Idade;
# 	Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é	uma combinação entre
# 	os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por 
# 	que ela pode ser calculada a qualquer momento.
import os
import time

lista_frutas = [{'codigo': 1,'descricao':   'Maçã', 'valor_energetico': 10, 'saude': 10 },
				{'codigo': 2,'descricao':'Morango', 'valor_energetico':  2, 'saude': 20 },
				{'codigo': 3,'descricao':  'Melão', 'valor_energetico': 30, 'saude': 40 } ]
	
lista_massas = [{'codigo': 1,'descricao':  'Lazanha', 'valor_energetico': 80, 'saude': 2},
				{'codigo': 2,'descricao': 'Macarrão', 'valor_energetico': 60, 'saude': 5},
				{'codigo': 3,'descricao': 'Panqueca', 'valor_energetico': 40, 'saude': 3} ]

lista_doces = [{'codigo': 1, 'descricao':          'Bala', 'valor_energetico': 20, 'saude': -2},
			   {'codigo': 2, 'descricao':     'Chocolate', 'valor_energetico': 20, 'saude':  1},
			   {'codigo': 3, 'descricao': 'Doce de Leite', 'valor_energetico': 20, 'saude': -8} ]
	
lista_bebidas = [{'codigo': 1, 'descricao': 'Refrigerante', 'valor_energetico': 40, 'saude': -20},
				 {'codigo': 2, 'descricao': 'Suco Natural', 'valor_energetico': 10, 'saude':   5},
				 {'codigo': 3, 'descricao':         'Água', 'valor_energetico':  2, 'saude':  30} ]

class BichinhoEletrônico():
	def __init__(self, nome='', fome=20, saude=80, idade=1):
		self.nome = nome
		self.fome = fome
		self.saude = saude
		self.idade = idade
		
	def limpar_tela(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')	
		print('-' *50,'\n')
		self.cara_bichinho()
		print('-' *50)

	def mostrar_bichinho(self):
		self.limpar_tela()
		if (self.idade >= 1) and (self.idade <= 3):
			classe = 'Categoria: Bebê'
		elif(self.idade >=4) and (self.idade <=10):
			classe = 'Categoria: Criança'
		elif(self.idade >= 11) and (self.idade <= 17):
			classe = 'Categoria: Adolescente'
		elif (self.idade >= 18) and (self.idade <= 25):
			classe = 'Categoria: Jovem'
		elif (self.idade >= 25) and (self.idade <= 60):
			classe = 'Categoria: Adulto'
		else:
			classe = 'Categoria: Idoso'
		print('\nNome  -------------> {}'    .format(self.nome) )
		print('Fome  -------------> {:<3} %' .format(self.fome) )
		print('Saúde -------------> {:<3} %' .format(self.saude))
		print('Idade -------------> {:<3}{:>25}' .format(self.idade, classe))
		print('-' *50)
		self.menu()
	
	def menu(self):
		print('[1] - Alimentar {}'           .format(self.nome))
		print('[2] - Dar remédio para {}'    .format(self.nome))
		print('[3] - Colocar {} para dormir' .format(self.nome))
		while True:
			opcao = int(input('\n>> '))
			if opcao == 1:
				self.alimentando_bichinho()
				break
			elif opcao == 2:
				print('Dando remédio') # +++++++++++++++++++++++++++++++++++++++++ FAZER O MENU
				break
			elif opcao == 3:
				if os.name == 'nt':
					os.system('cls')
				else:
					os.system('clear')
				print('-' *50, '\n')
				print('        (u_u)   {} dormindo...' .format(self.nome))
				print('-' *50)
				sono = ['ZZZZZzzzzzz......','ZZZZzzz...','ZZZzz..','Zz..','...']
				for i in range(0,5):
					print('\n', sono[i])
					time.sleep(0.8)
				time.sleep(1)
				input('\nDigite ENTER para acordar o {}   ' .format(self.nome))
				self.idade += 1
				if self.fome >= 50:
					self.fome = 100
				else:
					self.fome += 50
				if self.saude > 70:
					self.saude = 100
				else:
					self.saude += 30
				self.mostrar_bichinho()				
				break
			else:
				print('Dados Inválidos')
		
	def alterar_nome(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')		
		print('Bichinho Eletrônico')
		print('Lembre-se:\n> O bichinho fica 1 ano mais velho cada vez que dorme.')
		print('> Precisa alimentar o seu bichinho.\n> Cuide da saúde de seu bichinho.')
		print('-' *50)
		n = input('Dê um nome para o seu bichinho eletrônico: ')
		self.nome = n
		self.mostrar_bichinho()

	def cara_bichinho(self):
		if (self.fome >= 60) and (self.fome <= 100):
			if self.saude < 40:
				print('        (@_@)    {} está doente e com muita fome!' .format(self.nome))
			else:
				print('        (v_v)    {} está com muita fome!' .format(self.nome))
		elif (self.fome > 20) and (self.fome <= 59):
			if self.saude < 40:
				print('        (o_o)    {} está doente e começando a ficar com fome!' .format(self.nome))
			else:
				print('        (^_^)    {} está começando a ficar com fome!' .format(self.nome))
		else:
			if self.saude < 40:
				print('        (-_-)    {} está doente!' .format(self.nome))
			else:
				print('       \(^_^)/   {} está muito contente!' .format(self.nome))
	
	def alimentando_bichinho(self):
		self.limpar_tela()
		print('Alimente o {} '.format(self.nome))
		print('[1] - Frutas\n[2] - Massas\n[3] - Doces\n[4] - Bebidas\n')
		while True:
			opcao = int(input('>> '))
			if opcao == 1:
				self.limpar_tela()
				print('[1] - Frutas ( Tabela )\n\nCódigo  Descrição     Valor_energ  Saúde')
				print('-' *50)
				for i in lista_frutas:
					print('{:<8}{:<14}{:^11}{:^7}' .format(i['codigo'], i['descricao'], i['valor_energetico'], i['saude'] ))
				print('-' *50)
				self.comida(1)
				break
			elif opcao == 2:
				self.limpar_tela()
				print('[2] - Massas ( Tabela )\n\nCódigo  Descrição     Valor_energ  Saúde')
				print('-' *50)
				for i in lista_massas:
					print('{:<8}{:<14}{:^11}{:^7}' .format(i['codigo'], i['descricao'], i['valor_energetico'], i['saude'] ))
				print('-' *50)
				self.comida(2)
				break
			elif opcao == 3:
				self.limpar_tela()
				print('[3] - Doces ( Tabela )\n\nCódigo  Descrição     Valor_energ  Saúde')
				print('-' *50)
				for i in lista_doces:
					print('{:<8}{:<14}{:^11}{:^7}' .format(i['codigo'], i['descricao'], i['valor_energetico'], i['saude'] ))
				print('-' *50)
				self.comida(3)
				break
			elif opcao == 4:
				self.limpar_tela()
				print('[4] - Frutas ( Tabela )\n\nCódigo  Descrição     Valor_energ  Saúde')
				print('-' *50)
				for i in lista_bebidas:
					print('{:<8}{:<14}{:^11}{:^7}' .format(i['codigo'], i['descricao'], i['valor_energetico'], i['saude'] ))
				print('-' *50)
				self.comida(4)
				break
			else:
				print('Dados inválidos! ')
	
	def comida(self, dados_comida):
		if dados_comida == 1:
			while True:			
				opcao = int(input('\n>> '))
				if opcao > len(lista_frutas):
					print('Dados Inválidos! ')
				else:
					for i in lista_frutas:
						if i['codigo'] == opcao:
							self.fome = self.fome - i['valor_energetico']
							self.saude = self.saude + i['saude']
					if self.fome < 0:
						self.fome = 0
					break
			print('{} comendo ..... ' .format(self.nome))
			time.sleep(3)
			self.mostrar_bichinho()
		elif dados_comida == 2:
			while True:			
				opcao = int(input('\n>> '))
				if opcao > len(lista_frutas):
					print('Dados Inválidos! ')
				else:
					for i in lista_massas:
						if i['codigo'] == opcao:
							self.fome = self.fome - i['valor_energetico']
							self.saude = self.saude + i['saude']
					if self.fome < 0:
						self.fome = 0
					break
			print('{} comendo ..... ' .format(self.nome))
			time.sleep(3)
			self.mostrar_bichinho()
		elif dados_comida == 3:
			while True:			
				opcao = int(input('\n>> '))
				if opcao > len(lista_frutas):
					print('Dados Inválidos! ')
				else:
					for i in lista_doces:
						if i['codigo'] == opcao:
							self.fome = self.fome - i['valor_energetico']
							self.saude = self.saude + i['saude']
					if self.fome < 0:
						self.fome = 0
					break
			print('{} comendo ..... ' .format(self.nome))
			time.sleep(3)
			self.mostrar_bichinho()
		elif dados_comida == 4:
			while True:			
				opcao = int(input('\n>> '))
				if opcao > len(lista_frutas):
					print('Dados Inválidos! ')
				else:
					for i in lista_bebidas:
						if i['codigo'] == opcao:
							self.fome = self.fome - i['valor_energetico']
							self.saude = self.saude + i['saude']
					if self.fome < 0:
						self.fome = 0
					break
			print('{} bebendo ..... ' .format(self.nome))
			time.sleep(3)
			self.mostrar_bichinho()

b = BichinhoEletrônico()
b.alterar_nome()
