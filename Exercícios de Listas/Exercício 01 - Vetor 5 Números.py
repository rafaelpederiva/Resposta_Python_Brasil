#Exercício 01
#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
numbers = []
for i in range(0, 5):
    numbers.append(int(input('Informe o %dº número: ' %(i + 1))))
print('\n', numbers, '\n')