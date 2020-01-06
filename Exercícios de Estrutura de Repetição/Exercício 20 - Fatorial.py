#Exercício 20 
'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números
inteiros positivos e menores que 16.'''
n = 0
while (n <= 0):
	n = int(input('Digite um número para sabero o seu fatorial: '))
	if (n <= 0):
		print('Digite um valor maior do que zero!')
	else:
		fat = 1
		while (n > 1):
			fat = fat * n
			n = n - 1
		print('O fatorial é: ', fat)