#Exercício 08 
'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.'''
lista = []
for i in range(0,3): 
    produto = float(input('Digite o preço do %dº produto: ' %(i + 1)))
    lista.append(produto)
print('Você deve comprar o produto: R$ %2.2f' %min(lista))