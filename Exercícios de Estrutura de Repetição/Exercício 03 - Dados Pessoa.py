##Exercício 03 
'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''
class Validar_Dados():

    def __init__(self, nome, idade, salario, sexo, estado_civil):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.sexo = sexo
        self.estado_civil = estado_civil
    
    def dados_nome(self):        
        while True:
            n = input('Digite seu nome: ')
            if len(n) > 3:
                self.nome = n
                self.dados_idade()
                break
            else:
                print('Nome Inválido!!')

    def dados_idade(self):
        while True:
            i = int(input('Digite sua idade: '))
            if (i > 0) and (i < 150):
                self.idade = i
                self.dados_salario()
                break
            else:
                print('Idade Inválida!!')
    
    def dados_salario(self):
        while True:
            sl = float(input('Digite o seu salário: '))
            if sl > 0:
                self.salario = sl
                self.dados_sexo()
                break
            else:
                print('Salário Inválido!!')
    
    def dados_sexo(self):
        while True:
            sx = input('Digite qual é seu sexo [F] Feminino [M] Masculino: ').upper()
            if (sx == 'F') or (sx == 'M'):
                self.sexo = sx
                self.dados_civil()
                break
            else:
                print('Sexo Inválido!!')

    def dados_civil(self):
        print(  'Informe:\n' +
                '[S] - Solteiro(a)\n' +
                '[C] - Casado(a)\n' +
                '[D] - Divorciado(a)\n' +
                '[V] - Viúvo(a)' )
        while True:
            c = input('Digite seu estado civil: ').upper()
            if (c == 'S') or (c == 'C') or (c == 'D') or (c == 'V'):
                self.estado_civil = c
                self.imprimi_dados()
                break
            else:
                print('Estado civil inválido!!')
    
    def imprimi_dados(self):        
        print('')
        print('Relatório Geral')
        print('*' *30)
        print('%-16.16s  %-10.10s' %('Nome:', self.nome) )
        print('%-16.16s  %-10.0i' %('Idade:', self.idade) )
        print('%-16.16s  R$%-10.2f' %('Salário:', self.salario) )      
        lista1 = [{'sigla':'F', 'descrição': 'Feminino'},{'sigla':'M', 'descrição': 'Masculino'}]
        for i in lista1:
            if self.sexo == i['sigla']:
                print('%-16.16s  %-10.10s' %('Sexo:', i['descrição']) )     
        lista2 = [  {'sigla':'S', 'descrição': 'Solteiro(a)'},
                    {'sigla':'C', 'descrição': 'Casado(a)'},
                    {'sigla':'V', 'descrição': 'Viúvo(a)'},
                    {'sigla':'D', 'descrição': 'Divorciado(a)'}   ]
        for f in lista2:
            if self.estado_civil == f['sigla']:
                print('%-16.16s  %-13.13s \n\n' %('Estado Civil:', f['descrição']) )

v = Validar_Dados('P', 155, -5, 'P', 'A')
v.dados_nome()
