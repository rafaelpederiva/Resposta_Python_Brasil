#Exercício 02 
#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
#1ª) forma:
number = []
for i in range(0,10):
	number.append(int(input('Informe um número: ')))
print(number[::-1])
#2ª) forma:
number = []
for i in range(0,10):
	number.append(int(input('Informe um número: ')))
number.reverse()
print(number)