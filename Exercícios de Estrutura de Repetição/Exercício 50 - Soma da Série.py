#Exercício 50 
'''Imprima no final a soma da série.
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.'''
h = 1
n = 2
termos = int(input('Digite n: '))
lista_h = [1]
lista_n = []
print('\nH = 1', end=' + ')
for i in range(termos):    
    print('%i/%i' %(h, n), end='') 
    lista_h.append(h)
    lista_n.append(n)   
    if n == (termos + 1):
        print(' => ', end='')
    else:
        print(' + ', end='')
    n += 1
print('%i/' %sum(lista_h) + '%i' %sum(lista_n) +'\n')