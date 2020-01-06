#Exercício 17 
#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
#  Primeira forma de fazer:
numero = int(input('Digite um número para sabero o seu fatorial: '))
fatorial = 1
for i in range(1, numero + 1):
	fatorial = fatorial * i
print('O fatorial do número ', numero, 'é', fatorial)
#  Segunda forma de fazer:
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