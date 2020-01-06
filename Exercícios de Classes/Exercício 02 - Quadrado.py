#Exercício 02
'''Classe Quadrado: Crie uma classe que modele um quadrado:
	> Atributos: Tamanho do lado
	> Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''
class Quadrado():
    def __init__(self, lado = 0):
        self.lado = lado

    def mudarLado(self):
        troca = int(input('\nDigite o lado do quadrado: '))
        self.lado = troca

    def valorLado(self):
        print('\nO valor do lado do quadrado é {} e sua área {}'.format(self.lado, self.lado * self.lado))

def main():
    quadrado = Quadrado()
    quadrado.mudarLado()
    quadrado.valorLado()

main()
