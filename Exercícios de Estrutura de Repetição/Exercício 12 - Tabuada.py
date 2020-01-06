#Exercício 12 
'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual 
numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''
tb = int(input('Digite qual tabuada você quer saber: '))
n = 0
for i in range(0,10):
	n = n + 1
	print(tb, 'X', n, '=', (tb * n))