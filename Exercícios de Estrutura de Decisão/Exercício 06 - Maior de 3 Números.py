#Exercício 06
#Faça um Programa que leia três números e mostre o maior deles.
lista = []
for i in range(0,3):
    n = int(input('Digite o %dº número: ' %(i + 1)))
    lista.append(n)
print('O número: %d é o maior!' %max(lista))