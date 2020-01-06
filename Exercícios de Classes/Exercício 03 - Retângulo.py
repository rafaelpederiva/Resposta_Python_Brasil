#Exercício 03
'''Classe Retangulo: Crie uma classe que modele um retangulo:
	> Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
	> Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
	> Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
	Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''
class Retangulo():
    def __init__(self, comprimento = 0, largura = 0):
        self.comprimento = comprimento
        self.largura = largura

    def mudarValor(self):
        troca_comprimento = int(input('Digite o comprimento do local: '))
        troca_largura = int(input('Digite a largura do local: '))
        self.comprimento = troca_comprimento
        self.largura = troca_largura

    def retornaValor(self):
        area = self.comprimento * self.largura
        area_linear = (self.comprimento * 2) + (self.largura * 2)
        piso = area / 0.5
        rodape = area_linear / 0.5
        print('A área em metros quadrados do local é de {}\n'.format(area))
        print('Para essa área é preciso de %.f pisos e %.f rodapés.'%(piso,rodape))

retangulo = Retangulo()
retangulo.mudarValor()
retangulo.retornaValor()