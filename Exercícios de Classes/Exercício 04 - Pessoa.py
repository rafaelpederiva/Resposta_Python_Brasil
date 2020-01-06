#Exercício 04
'''Classe Pessoa: Crie uma classe que modele uma pessoa:
	> Atributos: nome, idade, peso e altura
	> Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que
	21 anos, ela deve crescer 0,5 cm.'''
class Pessoa():
    def __init__(self, nome='unknow', idade=0, peso=0, altura=0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, sumIdade):
        for i in range(sumIdade):
            self.idade += 1
            if self.idade < 21:
                self.crescer()

    def engordar(self, sumPeso):
        self.peso += sumPeso

    def emagrecer(self, subPeso):
        self.peso -= subPeso

    def crescer(self):
        self.altura += 0.05

pessoa = Pessoa('Pedro', 18, 55.7, 1.70)
pessoa.envelhecer(8)
pessoa.engordar(4.8)
print('\nNome: {}\nIdade: {}\nPeso: {}\nAltura: {}'.format(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura))
