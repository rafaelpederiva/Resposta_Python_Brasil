#Exercício 12 
'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende 
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é 
descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá
pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% 
    
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o 
    valor da hora é 5 e a quantidade de hora é 220.
           
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00 '''
class Folha_Pagamento():

    def __init__(self, hora, mes, salario_bruto, sindicato, ir, inss, fgts, porcentagem):
        self.hora = hora
        self.mes = mes
        self.salario_bruto = salario_bruto
        self.sindicato = sindicato
        self.ir = ir
        self.inss = inss
        self.fgts = fgts
        self.porcentagem = porcentagem

    def entrada_dados(self):
        while True:
            self.hora = int(input('Digite quanto ganha por hora: '))
            self.mes = int(input('Digite quantas horas você trabalha por mês: '))
            if (self.hora > 0) and (self.mes > 0):
                self.salario_bruto = self.hora * self.mes
                if self.salario_bruto <= 900:
                    self.porcentagem = 0.00
                elif (self.salario_bruto > 900) and (self.salario_bruto <= 1500):
                    self.porcentagem = 0.05
                elif (self.salario_bruto > 1501) and (self.salario_bruto <= 2500):
                    self.porcentagem = 0.10
                elif self.salario_bruto > 2500:
                    self.porcentagem = 0.20
                self.calculo_geral()
                break
            else:
                print('Dados inválidos!')

    def calculo_geral(self):
        self.sindicato = self.salario_bruto * 0.03
        self.fgts = self.salario_bruto * 0.11
        self.inss = self.salario_bruto * 0.10
        self.ir = self.salario_bruto * self.porcentagem
        self.imprime_resultado(0,0,0)

    def imprime_resultado(self, total_descontos, salario_liquido, porc):
        total_descontos = self.inss + self.ir
        salario_liquido = self.salario_bruto - total_descontos
        print('Salário Bruto          : R${0:9.2f}'        .format(self.salario_bruto))
        print('(-) IR ({0:2.0f}%)           : R${1:9.2f}'  .format(self.porcentagem * 100, self.ir))
        print('(-) INSS               : R${0:9.2f}'        .format(self.inss))
        print('FGTS (11%)             : R${0:9.2f}'        .format(self.fgts))
        print('Total de descontos     : R${0:9.2f}'        .format(total_descontos))
        print('Salário Líquido        : R${0:9.2f}'        .format(salario_liquido))
        
f = Folha_Pagamento(-1,-1,-1,-1,-1,-1,-1,-1)
f.entrada_dados()