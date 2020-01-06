#Exercício 13 
'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize
a função de potência da linguagem.'''
base = int(input('Digite o número base: '))
exp = 0
while (exp <= 0):
	exp = int(input('Digite o número expoente: '))
	if (exp <= 0):
		print('O espoente deve ser positivo!')
potencia = 1
for i in range(1, exp + 1):
	potencia = potencia * base
print(base, 'elevado a', exp, '=', potencia )
print()
print('Prova real: ', (base**exp))