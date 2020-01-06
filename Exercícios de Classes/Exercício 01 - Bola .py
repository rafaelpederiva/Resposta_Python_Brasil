#Exercício 01
'''Classe Bola: Crie uma classe que modele uma bola:
	> Atributos: Cor, circunferência, material
	> Métodos: trocaCor e mostraCor'''
class Bola():
    def __init__(self, cor = 'unknown',circunferencia = 0 ,material = 'unknown'):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self):
        while True:
            troca = input('\nDeseja trocar a cor da bola? digite [s / n] ')
            troca = troca.lower()
            if troca == 's':
                novaCor = input('Digite a nova cor para a bola: ')
                self.cor = novaCor
                self.mostraCor()
                break
            elif troca == 'n':
                print('A cor continua {}'.format(self.cor))
                break
            else:
                print('Dados incorretos! Digite "s" para sim e "n" para não.')
    
    def mostraCor(self):
        print('A cor da bola é: {}'.format(self.cor))

Bola.trocaCor()

# def main():
#     bola = Bola('Preta', 10, 'Couro')
#     bola.mostraCor()
#     bola.trocaCor()
# main()



