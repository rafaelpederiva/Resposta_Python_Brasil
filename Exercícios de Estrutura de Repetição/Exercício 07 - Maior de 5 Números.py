#Exercício 07 
#Faça um programa que leia 5 números e informe o maior número.
lista = []
for i in range (0,5):
    n = int(input('Digite um número: '))
    lista.append(n)
print('O maior número da lista é: ', max(lista))