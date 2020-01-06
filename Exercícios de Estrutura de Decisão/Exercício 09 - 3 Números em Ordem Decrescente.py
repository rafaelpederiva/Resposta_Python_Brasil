#Exercício 09 
#Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = []
for i in range(0,3):
    n = int(input('Digite o %dº número: ' %(i + 1)))
    lista.append(n)

lista.sort(key=int, reverse=True)

print('\nA ordem descrescente é: ', end='')
for f in range(len(lista)):
    print(lista[f],end=' ')