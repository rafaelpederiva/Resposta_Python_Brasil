#Exercício 01
#Faça um Programa que peça dois números e imprima o maior deles.
lista = []
for i in range(0,2):
    n = int(input('Digite o %dº número: ' %(i + 1)))
    lista.append(n)

print('O maior número é: ', max(lista))