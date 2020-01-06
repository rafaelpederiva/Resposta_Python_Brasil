#Exercício 05 
'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números 
IMPARES no vetor impar. Imprima os três vetores.'''
numeros = []
par = []
impar = []
for i in range(0,20):
    n = int(input('Insira um número: '))
    numeros.append(n)
    if (n % 2 == 0):
        par.append(n)
    else:
        impar.append(n)
print('Os números digitados foi: ', numeros)
print('Desse os números pares são: ', par)
print('E os números impar: ', impar)