#Exercício 09 
#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
lista = []
for i in range(0,10):
    numero = int(input('Insira um número: '))
    lista.append(numero**2)
print(lista)