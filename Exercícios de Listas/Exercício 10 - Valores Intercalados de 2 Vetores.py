#Exercício 10 
'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores.'''
vetor1 = []
vetor2 = []
for i in range(0,10):
    n1 = int(input('Isira o %dº valor para o vetor 1: ' %(i + 1)))
    n2 = int(input('Isira o %dº valor para o vetor 2: ' %(i + 1)))
    vetor1.append(n1)
    vetor2.append(n2)
vetor3 = []
for i in range(0,10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print('O vetor 1 é composto pelos elementos: ', vetor1)
print('O vetor 2 é composto pelos elementos: ',vetor2)
print('O dois vetores intercalados são: ', vetor3)