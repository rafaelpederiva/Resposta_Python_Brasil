#Exercício 02
'''Faça um programa para imprimir:
         1
         1   2
         1   2   3
         .....
        1   2   3   ...  n
     para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha. '''

def imprimir(numero):
   lista = []
   for i in range(1, numero + 1):
      print()
      lista.append(i)
      for i in range(len(lista)):
         print(lista[i], end=' ')

n = int(input('Informe um número: '))
imprimir(n)
